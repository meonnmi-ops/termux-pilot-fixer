import os

def pilot_fix():
    print("[*] Pilot Mode: Running Final Font Fix...")
    
    # Font path သတ်မှတ်ခြင်း
    home = os.path.expanduser("~")
    font_file = os.path.join(home, ".termux/font.ttf")
    
    if os.path.exists(font_file):
        print("[+] Found font.ttf. Reloading settings...")
        os.system("termux-reload-settings")
        print("[SUCCESS] Pilot has reloaded the system!")
    else:
        print("[-] Font file not found. Please run install.py first.")

if __name__ == "__main__":
    pilot_fix()
