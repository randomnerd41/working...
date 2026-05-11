import time
import os
import sys

# ============
# == PISTON ==
# ============
# info:
# alpha_patch1
# FOSS - AGPL 3.0
# classiccatlinux (randomnerd41)
# status: old patch


def update_debian_sudo():
    os.system("sudo apt update -y && sudo apt upgrade -y")

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def wait(wt):
    time.sleep(wt)
    
def osname():
    name = sys.platform
    print("Your OS is:", name)
    time.sleep(3)
    clear()
    
def cmd(c):
    os.system(c)

ms = lambda x: time.sleep(x / 1000)
