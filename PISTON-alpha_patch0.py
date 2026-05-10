import time
import os
import sys

# ============
# == PISTON ==
# ============
# info:
# alpha_patch0
# FOSS - AGPL 3.0
# classiccatlinux (randomnerd41)
# bugs: 0

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
    

