# File: main.py

import argparse
from modules.whois_module import run_whois_lookup
from modules.dns_module import run_dns_enum
from modules.subdomain_module import run_subdomain_enum
from modules.portscan_module import run_port_scan
from modules.banner_module import run_banner_grab
from modules.techdtect_module import run_tech_detect
from utils.logger import log_info

def main():
    parser = argparse.ArgumentParser(description="🔍 Custom Recon Tool by HK")
    
    # Passive Recon
    parser.add_argument("--whois", help="Perform WHOIS Lookup", action="store_true")
    parser.add_argument("--dns", help="Perform DNS Enumeration", action="store_true")
    parser.add_argument("--subdomain", help="Perform Subdomain Enumeration", action="store_true")
    
    # Active Recon
    parser.add_argument("--portscan", help="Perform Port Scanning", action="store_true")
    parser.add_argument("--banner", help="Perform Banner Grabbing", action="store_true")
    parser.add_argument("--tech", help="Perform Technology Detection", action="store_true")
    
    # Required domain/target
    parser.add_argument("--target", help="Target domain or IP (required)", required=True)
    
    args = parser.parse_args()

    log_info(f"[TOOL] Recon start horha hai for: {args.target}")
    
    if args.whois:
        run_whois_lookup(args.target)

    if args.dns:
        run_dns_enum(args.target)

    if args.subdomain:
        run_subdomain_enum(args.target)

    if args.portscan:
        run_port_scan(args.target)

    if args.banner:
        run_banner_grab(args.target)

    if args.tech:
        run_tech_detect(args.target)

    log_info(f"[TOOL] Recon complete hogya for: {args.target}")
    print("\n Recon complete. Report generated in 'reports' folder.")

if __name__ == "__main__":
    main()
