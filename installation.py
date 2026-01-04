#starting message
print("Welcome to the exigence executable installer, installation script")

#modules
import os

#run code
#update & upgrade
os.system("su sudo apt update && sudo apt upgrade")

#moves executable
os.system("mv exigence-executable-installer.py /usr/bin")

#moves desktop shortcut
os.system("mv exigence-executable-installer.desktop /usr/share/applications")

#removes traces of intervention
print("Coming soon!")



