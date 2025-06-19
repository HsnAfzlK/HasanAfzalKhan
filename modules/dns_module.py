import dns.resolver
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error
import socket

def run_dns_enum(domain):
    log_info(f"[DNS] DNS Enumeration start horha hai : {domain}")
    try:
        ip_address = socket.gethostbyname(domain)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = f"\n--- DNS Enumeration ---\nTime: {timestamp}\nDomain: {domain}\nResolved IP: {ip_address}\n"

        for record_type in ["A", "MX", "TXT", "NS"]:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                result += f"\n{record_type} Records:\n"
                for rdata in answers:
                    result += f" - {rdata.to_text()}\n"
            except Exception as e:
                result += f" - Failed to fetch {record_type} records: {e}\n"

        write_report(result)
        log_info("[DNS] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[DNS] Error during DNS Enumeration: {e}")
