import time
import os
import sys
#import subprocess

# ============
# == PISTON ==
# ============
# info:
# alpha_patch2
# FOSS - AGPL 3.0
# classiccatlinux (randomnerd41)
# status: waiting for patch 3/3

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def debian_autoremove_sudo():
    os.system("sudo apt autoremove -y")
    time.sleep(5)
    clear()

def update_debian_sudo():
    os.system("sudo apt update -y && sudo apt full-upgrade -y")
    time.sleep(5)
    clear()

def update_debian():
    os.system("apt update -y && apt full-upgrade -y")
    time.sleep(5)
    clear()

def update_fedora_sudo():
    os.system("sudo dnf update -y")
    time.sleep(5)
    clear()

def update_fedora():
    os.system("dnf update -y")
    time.sleep(5)
    clear()

def wait(wt):
    time.sleep(wt)
    
def osname():
    name = sys.platform
    print("OS = ", name)
    time.sleep(3)
    clear()
    
def cmd(c):
    os.system(c)

ms = lambda x: time.sleep(x / 1000)
