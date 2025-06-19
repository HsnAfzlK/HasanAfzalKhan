import requests
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error
import socket

def run_subdomain_enum(domain):
    log_info(f"[Subdomain] Starting Subdomain Enumeration for: {domain}")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            raise Exception("crt.sh API se data fetch nahi ho raha.")

        json_data = response.json()
        subdomains = set()
        for entry in json_data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())

        ip_map = {}
        for sub in subdomains:
            try:
                ip_map[sub] = socket.gethostbyname(sub)
            except:
                ip_map[sub] = "Resolution Failed"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = f"\n--- Subdomain Enumeration ---\nTime: {timestamp}\nDomain: {domain}\n"
        for sub, ip in ip_map.items():
            result += f" - {sub} => {ip}\n"

        write_report(result)
        log_info("[Subdomain] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[Subdomain] Exception occurred: {e}")
