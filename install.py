import os
import subprocess

def run_cmd(cmd):
    subprocess.run(cmd, shell=True)

print("--- Myanmar Font Fixer for Termux ---")
# 1. Folder structure ပြင်ဆင်ခြင်း
run_cmd("mkdir -p ~/.termux")
run_cmd("mkdir -p ~/.local/share/fonts")

# 2. Myanmar 3 Font ကို Download ဆွဲခြင်း
print("[*] Downloading Myanmar 3 Font...")
font_url = "https://github.com/thendu/myanmar-fonts/raw/master/Myanmar3.ttf"
run_cmd(f"wget {font_url} -O ~/.termux/font.ttf")
run_cmd("cp ~/.termux/font.ttf ~/.local/share/fonts/Myanmar3.ttf")

# 3. Termux Rendering properties ကို ပြင်ဆင်ခြင်း
print("[*] Optimizing Termux properties...")
properties_path = os.path.expanduser("~/.termux/termux.properties")
config_content = """
terminal-margin-horizontal=0
terminal-margin-vertical=0
allow-external-apps=true
"""
with open(properties_path, "a") as f:
    f.write(config_content)

# 4. System Refresh လုပ်ခြင်း
run_cmd("fc-cache -fv")
run_cmd("termux-reload-settings")

print("\n[+] Done! Please restart Termux for better rendering.")
