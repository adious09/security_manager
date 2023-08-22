import winreg
import os

def disable_usb_and_bluetooth():
    """
    Disable USB ports and Bluetooth by modifying the Windows Registry.
    This function sets the 'Start' value of USBSTOR and BthServ keys to 4.
    """
    try:
        # Registry keys for USB and Bluetooth services
        key_path_usb = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
        key_path_bt = r"SYSTEM\CurrentControlSet\Services\BthServ"
        
        # Disable USB Ports
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_usb, 0, winreg.KEY_SET_VALUE) as usb_key:
            winreg.SetValueEx(usb_key, "Start", 0, winreg.REG_DWORD, 4)
        
        # Disable Bluetooth
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_bt, 0, winreg.KEY_SET_VALUE) as bt_key:
            winreg.SetValueEx(bt_key, "Start", 0, winreg.REG_DWORD, 4)
    except Exception as e:
        print("Error:", e)

def block_website(website):
    """
    Block website access by adding an entry to the Windows hosts file.
    """
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    try:
        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(f"127.0.0.1 {website}\n")
    except Exception as e:
        print("Error:", e)

def main():
    # Apply security measures
    disable_usb_and_bluetooth()
    block_website("facebook.com")
    
    print("Security measures applied.")

if __name__ == "__main__":
    main()
