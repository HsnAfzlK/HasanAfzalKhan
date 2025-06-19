# File: utils/report.py

import os
from datetime import datetime

# Report file name (global)
REPORT_DIR = "reports"
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
REPORT_FILE = os.path.join(REPORT_DIR, f"RECON_HK_report_{timestamp}.txt")


def write_report(content):
    """Append content to the report file"""
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(content)
        f.write("\n" + "-" * 80 + "\n")
