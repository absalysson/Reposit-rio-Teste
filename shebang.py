#!/usr/bin/env python3
import os
import sys
def check_reboot()
"""returns true if teh com,puter has a pending reboot"""




return os.path.exist("/run/reboot-required")





def main():
    if check_reboot():
        print("Pending Reboot")
        sys.exit(l)

main()

