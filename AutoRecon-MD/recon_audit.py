import subprocess
import xml.etree.ElementTree as ET
import argparse
from datetime import datetime
import os


def run_nmap_scan(target):
    print(f"[*] Starting reconnaissance on target: {target}")
    xml_file = f"scan_{target.replace('.', '_')}.xml"

    # Running a Stealth SYN scan with Service Detection
    command = ["nmap", "-sS", "-sV", "-T4", "-oX", xml_file, target]

    try:
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

                    # Extract service info if available
                    service = port.find('service')
                    service_name = service.attrib.get('name') if service is not None else "Unknown"
                    service_version = service.attrib.get('version') if service is not None else ""
                    service_product = service.attrib.get('product') if service is not None else ""

                    open_ports.append({
                        "port": port_id,
                        "protocol": protocol,
                        "service": service_name,
                        "version": f"{service_product} {service_version}".strip()
                    })
    return open_ports


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

        f.write("## 2. Attack Surface Mapping\n")
        f.write("| Port | Protocol | Service | Version/Product |\n")
        f.write("|------|----------|---------|-----------------|\n")

        for p in open_ports:
            version_text = p['version'] if p['version'] else "Version hidden/Unknown"
            f.write(f"| {p['port']} | {p['protocol'].upper()} | {p['service']} | {version_text} |\n")

        f.write("\n## 3. Next Steps & Recommendations\n")
        f.write(
            "- **Service Auditing:** Cross-reference the identified versions against the National Vulnerability Database (NVD) for known CVEs.\n")
        f.write(
            "- **Firewall Rules:** Ensure any exposed administrative ports (e.g., SSH, RDP) are restricted to authorized IP addresses only.\n")

    print(f"[+] Professional Markdown report generated: {report_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Nmap Recon to Markdown Report")
    parser.add_argument("target", help="The IP address or domain to scan (e.g., 192.168.1.1)")
    args = parser.parse_args()

    # Step 1: Scan
    xml_output = run_nmap_scan(args.target)

    # Step 2: Parse
    extracted_data = parse_nmap_xml(xml_output)

    # Step 3: Report
    generate_markdown_report(args.target, extracted_data)

    # Optional Cleanup
    if os.path.exists(xml_output):
        os.remove(xml_output)