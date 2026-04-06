
# GitHub ကို Update လုပ်မယ်
git add pilot_engine.py
git commit -m "Add Pilot Engine for Auto-Fixing"
git push origin main
# GitHub ကို Update လုပ်မယ်
git add pilot_engine.py
git commit -m "Add Pilot Engine for Auto-Fixing"
git push origin mainimport os
import requests

def pilot_search_and_fix():
    print("[*] Pilot Mode: Checking Myanmar Font Rendering...")
    
    # ၁။ Font ရှိမရှိ အရင်စစ်မယ်
    if not os.path.exists(os.path.expanduser("~/.termux/font.ttf")):
        print("[!] Error: Font missing. Pilot is searching for a solution...")
        
        # ၂။ Web Search ခေါက်သလိုမျိုး Direct Link အသစ်ကို လှမ်းယူမယ်
        new_link = "https://github.com/thanyawzinmin/Myanmar-Unicode-Fonts/raw/master/Regular/Pyidaungsu-Regular.ttf"
        os.system(f"wget -q {new_link} -O ~/.termux/font.ttf")
        os.system("termux-reload-settings")
        print("[+] Pilot: Font Fixed and Reloaded!")
    else:
        print("[+] Pilot: System is stable.")

if __name__ == "__main__":
    pilot_search_and_fix()
