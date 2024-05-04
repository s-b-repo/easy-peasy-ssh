@echo off

@"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) -y" >nul 2>&1
SET "PATH=%PATH%;C:\ProgramData\chocolatey\bin"

choco install python -y

choco install wget -y

curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py

python get-pip.py

git clone https://github.com/s-b-repo/easy-peasy-ssh.git

cd easy-peasy-ssh

pip install pywin32

python Java-subprocess-manager.py
