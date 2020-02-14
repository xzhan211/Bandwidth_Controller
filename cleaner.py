'''
Application: Bandwidth Cleaner
Version: 1.0
Author: Xiaoyang Zhang
Email: xzhan211@binghamton.edu
'''

import subprocess

'''
step 1: check name of network card which you want to control
$ ip addr show
'''
network = 'eno1'

# For user: only set up above part.
# =================================================================
# For developer: below part.

parasClr = ['sudo', './wondershaper/wondershaper', '-c', '-a', '--']


def init(net):
    parasClr[4] = net


def clrSpeed():
    subprocess.check_call(parasClr)


def main():
    init(network)
    try:
        clrSpeed()
    except:
        print("An expected exception. Safe, don't worry : )")

if __name__ == "__main__":
    main()
