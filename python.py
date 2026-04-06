import os
import subprocess
import requests
from bs4 import BeautifulSoup

def search_fix(query):
    print(f"[*] Pilot searching for: {query}")
    # Google Search မှာ မြန်မာစာ fix နည်း လှမ်းရှာမယ်
    url = f"https://www.google.com/search?q={query}+termux+myanmar+font+fix"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    # ဒီနေရာမှာ Pilot က အဖြေထုတ်ပေးမယ့် logic ထည့်ရမှာပါ
    return "Suggestion: Use 'pkg install fontconfig' and 'termux-reload-settings'"

def run_pilot():
    print("--- MM-Autopilot Active ---")
    # လက်ရှိ Font status ကို စစ်မယ်
    status = os.popen("fc-list | grep -i myanmar").read()
    
    if not status:
        print("[!] Pilot detected: Myanmar Font missing!")
        solution = search_fix("installing+myanmar+font")
        print(f"[+] Pilot Recommendation: {solution}")
        # အလိုအလျောက် fix မယ့် command
        os.system("python install.py") 
    else:
        print("[+] Pilot: Myanmar Font is already present.")

if __name__ == "__main__":
    run_pilot()
