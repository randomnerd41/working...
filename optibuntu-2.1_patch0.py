import os
import time
import sys
import shutil

# ===============
# == Optibuntu ==
# =============== 

# info:
# Version 2.1-patch0
# FOSS - AGPL 3.0 
# made by classiccatlinux (randomnerd41).
# status: just added to working...
# no edits vs 2.0 yet.

# == config ==
devmode = False

# OS check
if not devmode:
    if sys.platform == "linux":
        if shutil.which("apt"):
            print("Welcome...")
            time.sleep(1)
            os.system("clear")
        else:       
            print("You are not on a Debian based linux system!")
            time.sleep(2)
            os.system("clear")
            exit()   
    else:
        print("For linux systems only!")
        time.sleep(2)
        exit()

# Start
if not devmode:
    print("===============")
    print("== Optibuntu ==")
    print("===============")
    print("v2.0 - classiccatlinux")
    in1 = input("start? (y/n): ")
    os.system('clear')

    if in1 == "n":
        print("Exiting...")
        time.sleep(1)
        exit()

    elif in1 == "y":
        print("Starting...")
        time.sleep(1)
        os.system('clear')
    else:
        print("Not a command at this time!")
        time.sleep(2)
        os.system('clear')
   
# Snap
print("== Snap ==")
print("Removing snap will remove firefox on ubuntu!")
print("options:")
print("1. Remove snap if its installed.")
print("2. Keep snap if its installed.")
print("3. quit")
print("/////////////////////////////")
inS = input("1, 2, or 3: ")

if inS == "1":
    if shutil.which("snap"):
        os.system("sudo systemctl disable snapd && sudo systemctl stop snapd")
        os.system("sudo apt purge snapd -y && rm -rf ~/snap")
        os.system("sudo rm -rf /snap /var/snap /var/lib/snapd")
        os.system("sudo apt-mark hold snapd")
        os.system("clear")
    else:
        print("Snap is not installed, skipping to next step...")
        time.sleep(2)
        os.system('clear')

elif inS == "2":
    print("Will not remove snap!")
    time.sleep(2)
    os.system('clear')
    
elif inS == "3":
    print("Quiting...")
    os.system('clear')
    time.sleep(2)
    exit()

else:
    print("Not a command at this time!")
    time.sleep(2)
    exit()

# Printing/Bluetooth
print("== Printing/bluetooth ==")
print("Would you like to turn off bluetooth/printing?")
print("Options:")
print("yes.")
print("no.")
print("///////////////////")
in2 = input("yes or no: ")

if in2 == "yes":
    if shutil.which("systemctl"):
        os.system("sudo systemctl disable bluetooth && sudo systemctl disable cups && sudo apt remove bluez blueman -y")
        os.system("clear")
    else:
        print("Systemd not detected, unable to disable bluetooth/printing.")
        time.sleep(5)
        os.system("clear")

elif in2 == "no":
    print("Will not disable bluetooth and printing.")
    time.sleep(2)
    os.system('clear')
    
else:
    print("Not a command at this time!")
    time.sleep(2)
    exit()

# Gnome
if shutil.which("gsettings"):
    print("== Gnome animations ==")   
    print("Would you like to turn off gnome animations?")
    print("Options:")
    print("yes.")
    print("no.")
    print("///////////////////")
    in3 = input("yes or no: ")

if in3 == "yes":
    os.system('clear')
    os.system("gsettings set org.gnome.desktop.interface enable-animations false")
    os.system('clear')
    
elif in3 == "no":
    print("Will not disable animations.")
    time.sleep(2)
    os.system('clear')
    
else:
    print("Not a command at this time!")
    time.sleep(1)
    exit()

# Fastfetch
print("== Fastfetch ==")
print("Would you like to install fastfetch?")
print("Options:")
print("yes.")
print("no.")
print("///////////////////")
ff = input("yes or no: ")

if ff == "yes":
    os.system("sudo apt install fastfetch -y")
    time.sleep(2)
    os.system('clear')
elif ff == "no":
    print("Will not install fastfetch.")
    time.sleep(2)
    os.system('clear')
else:
    print("Not a command at this time!")

# Updating/other
print("== Updating and ==")
print("== speeding up system ==")
print("this may take some time...")
print("////////////////////////////////")
time.sleep(2)
os.system('clear')
os.system("sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y")
if shutil.which("systemctl"):
    os.system("sudo apt install preload earlyoom -y && sudo apt install zram-tools -y && sudo systemctl enable zramswap && sudo systemctl start zramswap")    

# End
os.system("clear")
print("===============")
print("== Optibuntu ==")
print("===============")
print("//////////////////////////////////////////////////////////////////////////////")
os.system("fastfetch")
print("//////////////////////////////////////////////////////////////////////////////")
print("All done!")
print("thank you for using Optibuntu!")
print("You can now remove this program...")
exit()
