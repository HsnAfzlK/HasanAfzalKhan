#  Custom Reconnaissance Tool by HK

A modular and extensible reconnaissance tool for passive and active information gathering, developed as part of an internship. Built using Python and clean architecture principles.

---

1. ##  Features

This tool supports the following reconnaissance modules:

###  Passive Reconnaissance

* **WHOIS Lookup** — Retrieve domain registration information
* **DNS Enumeration** — Fetch A, MX, NS records of target
* **Subdomain Enumeration** — Discover subdomains using a wordlist

###  Active Reconnaissance

* **Port Scanning** — Scan open ports on target host
* **Banner Grabbing** — Grab service banners from open ports
* **Technology Detection** — Detect frontend/backend technologies (using WebTech But you have to put your Own API Key into the code in techdtect_module.py file)

---

2. ##  Installation

  **Clone the repo** or manually create the folder structure:

```bash
   git clone git clone https://github.com/HsnAfzlK/H-K
   cd RECON_HK

3. ## Installation Dependencies
   install -r requirements.txt

4. ## Usage Guide

## Run any individual module:
   python main.py --whois --target example.com


## Run multiple modules:
   python main.py --whois --dns --portscan --target example.com


## Run full recon:
   python main.py --whois --dns --subdomain --portscan --banner --tech --target example.com


5. ## Project Architecture/Struture

Recon_HK/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── whois_module.py
│   ├── dns_module.py
│   ├── subdomain_module.py
│   ├── portscan_module.py
│   ├── banner_module.py
│   └── techdetect_module.py
│
├── utils/
│   ├── logger.py
│   └── report.py
│
└── reports/
    └── HK_recon_report_<timestamp>.txt

 6. ## Logging & Verbosity
    Each module includes:

log_info → Informational logs

log_error → Errors in execution
Logs printed to terminal with timestamps.
>>>>>>> 27cf813 (initial commit of custom recon tool)
