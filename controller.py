'''
Application: Bandwidth Controller
Version: 1.0
Author: Xiaoyang Zhang
Email: xzhan211@binghamton.edu
'''

import subprocess
import csv
import time

'''
step 1: check name of network card which you want to control
$ ip addr show
'''
network = 'eno1'

'''

step 2: DIY csv file 'configuration.csv' with tx/rx rate and time.

example:
1024,1024,10
2048,2048,20
...
4096,2048,30

explanation:
upload speed(kbps), download speed(kbps), time of duration(second)
'''
fileName = 'configuration.csv'


# For user: only set up above part.
# =================================================================
# For developer: below part.

parasSet = ['sudo', './wondershaper/wondershaper', '-a', '--', '-u', '----', '-d', '----']
parasClr = ['sudo', './wondershaper/wondershaper', '-c', '-a', '--']

arrTx = []
arrRx = []
arrTime = []


def init(net):
    parasSet[3] = net
    parasClr[4] = net


def readCSV(path):
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp = row[0].split(',')
            arrTx.append(temp[0])
            arrRx.append(temp[1])
            arrTime.append(int(temp[2]))


def setSpeed(tx, rx):
    parasSet[5] = tx
    parasSet[7] = rx
    subprocess.check_call(parasSet)


def clrSpeed():
    subprocess.check_call(parasClr)


def loopRun(tx, rx, ti):
    try:
        print("tx: " + repr(tx) + "  rx: " + repr(rx) + "  time: " + repr(ti))
        setSpeed(tx, rx)
        time.sleep(ti)
        clrSpeed()
    except:
        print("An expected exception. Safe, don't worry : )")
    #make sure hardware (network card) has enough time to clean registers.
    time.sleep(1)


def main():
    init(network)
    readCSV(fileName)
    l = len(arrTx)

    try:
        clrSpeed()
    except:
        print("An expected exception. Safe, don't worry : )")

    while(1):
        print("in while loop!")
        for i in range(0, l):
            loopRun(arrTx[i], arrRx[i], arrTime[i])

if __name__ == "__main__":
    main()
