# AutoRecon-MD: Automated Vulnerability Reconnaissance

An automated security reconnaissance tool designed to bridge the gap between network scanning and vulnerability reporting.

##  What it does
1. **Network Discovery:** Executes stealthy Nmap SYN scans to identify open ports and services.
2. **Data Parsing:** Automatically parses raw XML scan data into actionable insights.
3. **Vulnerability Correlation:** Requests from Shodan's CVE (Common Vulnerability and Exploits) API to crossreference versions with known vulnerabilities.
4. **Professional Reporting:** Generates a structured Markdown report for stakeholders.

##  How to use it
1. Install dependencies From requirements.txt
   