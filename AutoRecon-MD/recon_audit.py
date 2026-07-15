import subprocess
import xml.etree.ElementTree as ET
import argparse
from datetime import datetime
import os
import requests


def run_nmap_scan(target):
    print(f"[*] Starting reconnaissance on target: {target}")
    xml_file = f"scan_{target.replace('.', '_')}.xml"

    # Running Stealth SYN scan
    command = ["nmap", "-sS", "-sV", "-T4", "-oX", xml_file, target]

    try:
        # Note: Needs sudo for SYN scan
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        print(f"[+] Nmap scan complete. Raw data saved to {xml_file}")
        return xml_file
    except FileNotFoundError:
        print("[-] Error: Nmap is not installed or not in your system PATH.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[-] Nmap scan failed: {e}")
        exit(1)


def parse_nmap_xml(xml_file):
    print("[*] Parsing XML data...")
    tree = ET.parse(xml_file)
    root = tree.getroot()

    open_ports = []

    for host in root.findall('host'):
        for ports in host.findall('ports'):
            for port in ports.findall('port'):
                state = port.find('state').attrib.get('state')
                if state == 'open':
                    port_id = port.attrib.get('portid')
                    protocol = port.attrib.get('protocol')

                    service = port.find('service')
                    service_name = service.attrib.get('name') if service is not None else "Unknown"
                    service_version = service.attrib.get('version') if service is not None else ""
                    service_product = service.attrib.get('product') if service is not None else ""

                    open_ports.append({
                        "port": port_id,
                        "protocol": protocol,
                        "service": service_name,
                        "product": service_product,
                        "version": service_version
                    })
    return open_ports


#API database lookup
def fetch_cves_for_service(product, version):
    """
    Queries Shodan's free CVEDB API to check for public CVEs
    associated with the discovered service name and version.
    """
    if not product or not version:
        return []


    cpe = f"cpe:2.3:a::{product.lower()}:{version.lower()}"
    api_url = f"https://cvedb.shodan.io/cves?cpe23={cpe}"

    try:
        print(f"[*] Querying vulnerability database for {product} {version}...")
        response = requests.get(api_url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            #Extracting only upto 3 Major Vulnerabilities
            cves = []
            matches = data.get("matches", [])
            for item in matches[:3]:
                cves.append({
                    "id": item.get("cve_id"),
                    "summary": item.get("summary", "No description available."),
                    "severity": item.get("cvss", "N/A")
                })
            return cves
    except Exception as e:
        print(f"[-] API query failed for {product}: {e}")

    return []




def generate_markdown_report(target, open_ports):
    report_name = f"Recon_Report_{target.replace('.', '_')}.md"
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_name, "w") as f:
        f.write(f"# Automated Vulnerability Reconnaissance Report\n\n")
        f.write(f"**Target:** `{target}`\n")
        f.write(f"**Scan Date:** {date_str}\n\n")

        f.write("## 1. Executive Summary\n")
        f.write(f"An automated perimeter scan was conducted against `{target}`. ")
        f.write(f"The scan successfully identified **{len(open_ports)}** open ports exposing network services.\n\n")

        f.write("## 2. Attack Surface Mapping & CVE Correlation\n")
        f.write("| Port | Protocol | Service | Version | Known Vulnerabilities Found |\n")
        f.write("|------|----------|---------|---------|-----------------------------|\n")

        for p in open_ports:
            product_name = p['product'] if p['product'] else p['service']
            version_text = p['version'] if p['version'] else "Unknown"

            # Fetch real vulnerabilities for this port
            cve_list = fetch_cves_for_service(p['product'], p['version'])

            if cve_list:
                cve_details = ""
                for cve in cve_list:
                    cve_details += f"CRITICAL **{cve['id']}** (CVSS: {cve['severity']})<br>*{cve['summary'][:100]}...*<br><br>"
            else:
                cve_details = "SAFE No immediate CVEs found in quick query."

            f.write(f"| {p['port']} | {p['protocol'].upper()} | {p['service']} | {version_text} | {cve_details} |\n")

        f.write("\n## 3. Next Steps & Recommendations\n")
        f.write("- **Service Patching:** Prioritize upgrading any services flagged with active CVEs (marked with CRITICAL).\n")
        f.write(
            "- **Port Minimization:** Disable or filter any exposed ports that are not strictly necessary for production operations.\n")

    print(f"[+] Professional Markdown report generated: {report_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Nmap Recon to Markdown Report")
    parser.add_argument("target", help="The IP address or domain to scan (e.g., 192.168.1.1)")
    args = parser.parse_args()

    xml_output = run_nmap_scan(args.target)
    extracted_data = parse_nmap_xml(xml_output)
    generate_markdown_report(args.target, extracted_data)

    if os.path.exists(xml_output):
        os.remove(xml_output)
