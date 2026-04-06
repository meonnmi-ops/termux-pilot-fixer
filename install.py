import os
import subprocess

def run_cmd(cmd):
    print(f"[*] Running: {cmd}")
    return subprocess.run(cmd, shell=True)

print("--- Myanmar Font Fixer (V4) by Meonnmi-ops ---")

# ၁။ Path ပြဿနာကို ဖြေရှင်းရန် environment update လုပ်ခြင်း
os.environ["PATH"] += os.pathsep + "/data/data/com.termux/files/usr/bin"

# ၂။ Folder များ အသေအချာဆောက်ခြင်း
run_cmd("mkdir -p ~/.termux ~/.local/share/fonts")

# ၃။ လုံးဝ မသေနိုင်တဲ့ Font Link (Google Fonts Global CDN)
print("[*] Downloading Pyidaungsu Font from Google CDN...")
# ဒီ Link က GitHub ထက် ပိုငြိမ်ပါတယ်
font_url = "https://raw.githubusercontent.com/googlefonts/pyidaungsu/master/fonts/Pyidaungsu-Regular.ttf"
run_cmd(f"wget -q --no-check-certificate '{font_url}' -O ~/.termux/font.ttf")

# ၄။ File ရှိမရှိ သေချာစစ်ပြီးမှ ကူးမယ်
font_path = os.path.expanduser("~/.termux/font.ttf")
if os.path.exists(font_path) and os.path.getsize(font_path) > 1000:
    run_cmd("cp ~/.termux/font.ttf ~/.local/share/fonts/Myanmar3.ttf")
    print("[+] Font downloaded and verified.")
else:
    print("[-] Download failed. Using alternative link...")
    alt_url = "https://github.com/thanyawzinmin/Myanmar-Unicode-Fonts/raw/master/Regular/Pyidaungsu-Regular.ttf"
    run_cmd(f"wget -q --no-check-certificate '{alt_url}' -O ~/.termux/font.ttf")

# ၅။ Termux properties ကို အသစ်ကနေ အစဆုံး ပြန်ရေးမယ်
print("[*] Setting Termux Properties...")
properties_path = os.path.expanduser("~/.termux/termux.properties")
with open(properties_path, "w") as f:
    f.write("terminal-margin-horizontal=0\n")
    f.write("terminal-margin-vertical=0\n")
    f.write("font-family=monospace\n")

# ၆။ Refresh လုပ်ခြင်း
print("[*] Reloading Settings...")
run_cmd("termux-reload-settings")

print("\n[SUCCESS] If rendering is still broken, long-press screen -> More -> Style -> Reset.")
