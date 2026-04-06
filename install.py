import os
import subprocess

def run_cmd(cmd):
    print(f"[*] Running: {cmd}")
    # shell=True သုံးပြီး error ဖြစ်ရင်လည်း ဆက်သွားအောင် လုပ်ထားတယ်
    return subprocess.run(cmd, shell=True)

print("--- Myanmar Font Fixer (V3 - Stable) by Meonnmi-ops ---")

# ၁။ Packages တွေကို Force Install လုပ်မယ်
print("[*] Updating and installing packages...")
run_cmd("pkg update -y && pkg install fontconfig wget -y")

# ၂။ Folder များဆောက်မယ်
run_cmd("mkdir -p ~/.termux")
run_cmd("mkdir -p ~/.local/share/fonts")

# ၃။ လုံးဝမသေနိုင်တဲ့ Font Link ကို သုံးမယ် (Direct Download)
print("[*] Downloading Myanmar Unicode Font...")
# Pyidaungsu Official Stable Link
font_url = "https://github.com/googlefonts/pyidaungsu/raw/main/fonts/Pyidaungsu-Regular.ttf"
run_cmd(f"wget --no-check-certificate '{font_url}' -O ~/.termux/font.ttf")

# ၄။ Font ဖိုင်ရှိမရှိ စစ်မယ်
if os.path.exists(os.path.expanduser("~/.termux/font.ttf")):
    run_cmd("cp ~/.termux/font.ttf ~/.local/share/fonts/Myanmar3.ttf")
    print("[+] Font download successful!")
else:
    print("[-] Font download failed. Please check internet.")

# ၅။ Termux Config ပြင်ဆင်ခြင်း
properties_path = os.path.expanduser("~/.termux/termux.properties")
with open(properties_path, "w") as f:
    f.write("terminal-margin-horizontal=0\n")
    f.write("terminal-margin-vertical=0\n")

# ၆။ Refresh လုပ်ခြင်း (Path ကိုပါ တိုက်ရိုက်ခေါ်မယ်)
print("[*] Refreshing Settings...")
run_cmd("/data/data/com.termux/files/usr/bin/fc-cache -fv || fc-cache -fv")
run_cmd("termux-reload-settings")

print("\n[SUCCESS] Restart Termux (Force Stop) to see the magic!")
