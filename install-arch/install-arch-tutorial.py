print("helllinux tutorial to install Arch. Should work for most cases, if it does not, please refer to Archwiki: ")
print(" ")

lang     = "us" if input("lang [(S)e/(u)s]: ").strip().lower() == "u" else "se"
hwname   = input(wifi-hardware-name (default wlan0): ")
hwname   = "wlan0" if len(hwname) > 0 else hwname
wifiname = input("wifi-name: ")
wifipw   = input("wifi-password: ")



if lang == "se":
    print("loadkeys se-lat6")

print("iwctl")
print(f"station {hwname} scan")
print(f"station {hwname} connect {wifiname} --passphrase {wifipw}")
print("exit")
print("archinstall")
