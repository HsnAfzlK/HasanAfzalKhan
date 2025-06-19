import socket
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error

def run_port_scan(domain, ports=[21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]):
    log_info(f"[Port Scan] Starting port scan for: {domain}")
    try:
        ip = socket.gethostbyname(domain)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = f"\n--- Port Scan ---\nTime: {timestamp}\nDomain: {domain}\nResolved IP: {ip}\n"
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                sock.connect((ip, port))
                result += f"[+] Port {port} is OPEN\n"
            except:
                result += f"[-] Port {port} is CLOSED or FILTERED\n"
            finally:
                sock.close()

        write_report(result)
        log_info("[Port Scan] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[Port Scan] Error during port scan: {e}")
