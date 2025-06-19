import socket
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error

def run_banner_grab(domain, ports=[21, 22, 25, 80, 110, 143, 443, 8080]):
    log_info(f"[Banner Grabbing] Start horhi hai for: {domain}")
    try:
        ip = socket.gethostbyname(domain)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = f"\n--- Banner Grabbing ---\nTime: {timestamp}\nDomain: {domain}\nResolved IP: {ip}\n"

        for port in ports:
            try:
                sock = socket.socket()
                sock.settimeout(2)
                sock.connect((ip, port))
                banner = sock.recv(1024).decode(errors="ignore").strip()
                result += f"[+] Port {port} Banner: {banner}\n"
                sock.close()
            except Exception as e:
                result += f"[-] Port {port} Banner: Nahi mila ya Error: {e}\n"

        write_report(result)
        log_info("[Banner Grabbing] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[Banner Grabbing] Error during banner grabbing: {e}")
