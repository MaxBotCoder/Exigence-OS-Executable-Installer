#starting message
print("Welcome to the exigence executable installer, installation script v2")

#modules
import os

#run code
#grants root
os.systsem("su")

#update & upgrade
os.system("apt update && apt upgrade")

#moves executable
os.system("mv exigence-executable-installer.py /usr/bin")

#moves desktop shortcut
os.system("mv exigence-executable-installer.desktop /usr/share/applications")

#removes traces of intervention
print("Coming soon!")






