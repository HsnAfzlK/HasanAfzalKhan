import whois
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error
import socket

def run_whois_lookup(domain):
    log_info(f"[WHOIS] WHOIS lookup start horha hai : {domain}")
    try:
        data = whois.whois(domain)
        ip_address = socket.gethostbyname(domain)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = f"""
--- WHOIS Lookup ---
Time: {timestamp}
Domain: {domain}
Resolved IP: {ip_address}
Registrar: {data.registrar}
Creation Date: {data.creation_date}
Expiration Date: {data.expiration_date}
Name Servers: {data.name_servers}
Emails: {data.emails}
"""
        write_report(result)
        log_info("[WHOIS] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[WHOIS] Error during WHOIS lookup: {e}")
