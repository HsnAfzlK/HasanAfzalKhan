import requests
from datetime import datetime
from utils.report import write_report
from utils.logger import log_info, log_error

def run_tech_detect(domain):
    log_info(f"[Tech Detection] Start horhi hai for: {domain}")
    try:
        url = f"https://api.wappalyzer.com/lookup/v2/?urls=https://{domain}"
        headers = {
            'x-api-key': 'YOUR_API_KEY_HERE'  # Replace this with your actual Wappalyzer API key
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = f"\n--- Technology Detection ---\nTime: {timestamp}\nDomain: {domain}\n"

        if data and isinstance(data, list) and 'technologies' in data[0]:
            tech_list = data[0]['technologies']
            for tech in tech_list:
                result += f"[+] {tech.get('name')} - {tech.get('categories', [{}])[0].get('name', 'Unknown')}\n"
        else:
            result += "[-] Koi technology detect nahi hui ya response empty tha.\n"

        write_report(result)
        log_info("[Tech Detection] Report write ho gayi successfully.")
    except Exception as e:
        log_error(f"[Tech Detection] Error during technology detection: {e}")
