#starting message
print("Welcome to the exigence executable installer, installation script v3")

#root confirmation
if os.geteuid != 0:
  print("Please run this program with elevated root privaleges. On debian this can be done via su, on ubuntu this is done via sudo su.")
  quit()

#modules
import os

#run code
#update & upgrade
os.system("apt update && apt upgrade")

#moves executable
os.system("mv exigence-executable-installer.py /usr/bin")

#moves desktop shortcut
os.system("mv exigence-executable-installer.desktop /usr/share/applications")

#removes traces of intervention
print("Coming soon!")











