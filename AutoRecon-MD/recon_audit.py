import os
import subprocess
import argparse
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def do_scan(target):
    print(f"scanning {target}...")
    xml_file = f"scan_{target.replace('.', '_')}.xml"

    # -sS usually needs sudo
    cmd = ["nmap", "-sS", "-sV", "-T4", "-oX", xml_file, target]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        return xml_file
    except FileNotFoundError:
        print("error: nmap isn't installed")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"scan failed: {e}")
        exit(1)


def parse_ports(xml_file):
    tree = ET.parse(xml_file)
    ports = []

    # flatten the messy xml tree lookup
    for p in tree.getroot().findall('.//port'):
        if p.find('state').get('state') == 'open':
            svc = p.find('service')
            ports.append({
                "port": p.get('portid'),
                "proto": p.get('protocol'),
                "service": svc.get('name') if svc is not None else "Unknown",
                "product": svc.get('product') if svc is not None else "",
                "version": svc.get('version') if svc is not None else ""
            })
    return ports


def get_cves(prod, ver):
    if not prod or not ver:
        return []

    # hacky cpe string but shodan usually accepts it
    cpe = f"cpe:2.3:a::{prod.lower()}:{ver.lower()}"
    url = f"https://cvedb.shodan.io/cves?cpe23={cpe}"

    try:
        print(f"checking vulns for {prod} {ver}...")
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()
            # grab top 3 so we don't flood the report
            return [{
                "id": x.get("cve_id"),
                "summary": x.get("summary", "No desc"),
                "severity": x.get("cvss", "N/A")
            } for x in data.get("matches", [])[:3]]

    except Exception as e:
        print(f"api error for {prod}: {e}")

    return []


def build_report(target, ports):
    fname = f"recon_{target.replace('.', '_')}.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(fname, "w") as f:
        f.write(f"# Recon Report: {target}\n")
        f.write(f"**Date:** {now}\n\n")
        f.write(f"Found **{len(ports)}** open ports.\n\n")

        f.write("| Port | Protocol | Service | Version | Vulnerabilities |\n")
        f.write("|---|---|---|---|---|\n")

        for p in ports:
            ver = p['version'] or "Unknown"
            cves = get_cves(p['product'], p['version'])

            if cves:
                details = "".join(
                    [f"CRITICAL **{c['id']}** (CVSS: {c['severity']})<br>*{c['summary'][:100]}...*<br><br>" for c in
                     cves])
            else:
                details = "No obvious CVEs found."

            f.write(f"| {p['port']} | {p['proto'].upper()} | {p['service']} | {ver} | {details} |\n")

        f.write("\n## Next Steps\n")
        f.write("- Patch anything marked CRITICAL immediately.\n")
        f.write("- Close exposed ports that aren't actively used.\n")

    print(f"done! report saved to {fname}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="IP or domain to scan")
    args = parser.parse_args()

    xml_out = do_scan(args.target)
    ports_data = parse_ports(xml_out)
    build_report(args.target, ports_data)

    # cleanup
    if os.path.exists(xml_out):
        os.remove(xml_out)