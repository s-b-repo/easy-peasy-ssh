@echo off

@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" >nul 2>&1
SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

REM Install Python
choco install python -y

REM Install git
choco install git -y

REM Download the get-pip.py script
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py

REM Install pip
python get-pip.py

REM Clone the Git repository
git clone https://github.com/coolst3r/db1.git

REM Change directory to the cloned repository
cd db1

REM Install required Python packages
pip install pywin32

REM Run the Python script
python lolz.py
