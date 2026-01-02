#welcome message
print("Welcome to Exegence-OS-executable-installer version 0.1 alpha")
print("\nRight click and press copy on the executable then paste it in the terminal below.\n")
print("Supported executables are: .debs, .appiamge, .run and flatpaks")

# modules
import os

#variables
#command input variable
commands = ""

#unrecomended files
unrecomended_file = ["NVIDIA","balena-etcher"]

#special installation method files
special_files = ["DaVinci_Resolve"]

#is typical
typical_file = False

#file name input
filename = ""

#functions
#help menu
def help():
    print("hello")

def detect_executable_name_start():
    iterations = 0
    for x in commands:
        iterations -= 1
        if commands[iterations] == "/":
            filename = commands[iterations+1:]
            print(filename)
            quit()

def scan_executable_name():
    iterations = 0
    for x in filename:
        iterations += 1
        if filename[0:iterations] == unrecomended_file[0]:
            print("An unrecomended appilcation has been detected.\nExigence os recomends you use the built in usb flashing utility instead.\nHowever if you still wish to install this driver please use the standard installation method.")
        elif filename[0:iterations] == unrecomended_file[1]:
            print("An unrecomended nvidia driver has been detected.\nExigence os recomends you use the built in driver installation utility for nvidia driver.\nHowever if you still wish to install this driver please use the standard terminal method.")
        elif filename[0:iterations] == special_files[1]:
            print("installing davinci resolve")
        else:
            typical_file = True            

#install deb package
def install_deb():
    os.system(f"su && apt update && sudo apt upgrade -y && sudo dpkg -i {commands} -y")
    print(".deb successfully installed!")
    quit()

#install app image
def install_appimage():
    detect_executable_name_start()
    scan_executable_name()
    if typical_file is True:
        os.system(f"su && sudo apt update && sudo apt upgrade -y && sudo ./{commands}")

#general install .run file
#davinci resolve installation automation
def install_davinc_resolve():
    print("filler")

#standard .run file automation
def install_run():
    detect_executable_name_start()
    scan_executable_name()
    if typical_file is True:
        os.system(f"su && sudo apt update && sudo apt upgrade -y && sudo ./{commands}")

#install flatpak
def install_flatpak():
    print("filler")

#install elf
def install_elf():
    print("Elf not supported yet!")

#file input
def file_input(command):
    if command[-4:] == ".zip":
        print(".zip files are not supported please extract the .zip file before hand \nby right clicking on it then clicking the extract button.")
    elif command[-7:] == ".tar.xz":
        print(".tar.xz files are not supported please extract the .tar.xz file before hand \nby right clicking on it then clicking the extract button.")
    elif command[-3:] == ".7z":
        print(".7z files are not supported please extract the .7z file before hand \nby right clicking on it then clicking the extract button.")
    elif command[-4:] == ".deb":
        print(f"Proceeding the installation of {command}")
        install_deb()
    elif command[-4:] == ".appimage":
        print(f"Proceeding the installation of {command}")
        install_appimage()
    elif command[-4:] == ".run":
        print(f"Proceeding the installation of {command}")
        install_run()
    elif command[-11:] == ".flatpakref":
        print(f"Proceeding the installation of {command}")
        install_flatpak()
    else:
        print("Unrecognised file type.")

#command inputs
def command_input(command):
    if command.lower() == "help":
        help()
    elif os.path.exists(command):
        file_input(command)
    else:
        print("file or command does not exist")
        
#calling functions
#terminal popup
while commands != "exit" or "quit":
    commands = input("Input name of file to install: ")
    command_input(commands)
