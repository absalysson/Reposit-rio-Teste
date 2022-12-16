#!/usr/bin/env python3
import os
import sys
import shutil

def check_reboot():

#returns true if the  computer has a pending reboot
#adicionando comentario

return os.path.exists("/run/reboot-required")


def check_disk_full(diskn ming_gb, min_percent):
    '''retorna verdadeiro se não há espaço suficiente e falso para outro jeito'''
    du = shutil.disk_usage(disk)
    #calcula a porcetagem de espaço livre
    percent_free = 100 * du.free / du.total
    #calcula quantos GBs tem livre
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def main():
    if check_reboot():
        print('pending reboot')
        sys.exit(1)
    if check_disk_full(disk="/",min_gb=2,min_percent=10):
        print("Disk Full")
        sys.exit(1)
    
    print("Everything Ok")
    sys.exit(0)
    
