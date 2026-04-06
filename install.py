import os
import subprocess

def run_cmd(cmd):
    print(f"[*] Running: {cmd}")
    subprocess.run(cmd, shell=True)

print("--- Myanmar Font Fixer (V2) by Meonnmi-ops ---")

# ၁။ လိုအပ်တဲ့ packages တွေကို အရင်သွင်းမယ်
print("[*] Installing required packages (fontconfig, wget)...")
run_cmd("pkg install fontconfig wget -y")

# ၂။ Folder structure ပြင်ဆင်ခြင်း
run_cmd("mkdir -p ~/.termux")
run_cmd("mkdir -p ~/.local/share/fonts")

# ၃။ Myanmar 3 Font (သို့မဟုတ် အစားထိုး Unicode Font) ကို Download ဆွဲခြင်း
# Link အသစ်ပြောင်းထားပါတယ်
print("[*] Downloading Myanmar Font...")
font_url = "https://github.com/googlefonts/pyidaungsu/raw/master/fonts/Pyidaungsu-2.5.3_Regular.ttf"
run_cmd(f"wget --no-check-certificate {font_url} -O ~/.termux/font.ttf")
run_cmd("cp ~/.termux/font.ttf ~/.local/share/fonts/Myanmar3.ttf")

# ၄။ Termux Rendering properties ကို ပြင်ဆင်ခြင်း
print("[*] Optimizing Termux properties...")
properties_path = os.path.expanduser("~/.termux/termux.properties")
config_content = "\nterminal-margin-horizontal=0\nterminal-margin-vertical=0\n"
with open(properties_path, "a") as f:
    f.write(config_content)

# ၅။ System Refresh လုပ်ခြင်း
print("[*] Refreshing font cache...")
run_cmd("fc-cache -fv")
run_cmd("termux-reload-settings")

print("\n[+] SUCCESS! Please restart Termux (Force Stop and Open).")
