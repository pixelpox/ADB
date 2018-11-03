import os
import time
import subprocess
from pullImage import pullImage
from clickBillboard import *
from findImage import templateMatch
from clicker import adbTapScreen

def myinit():
    subprocess.Popen('powershell.exe adb shell monkey -p com.cherrypickgames.myhospital -v 500')


#rewards
def getReward():
    pullImage()
    #clickLocation = findBillBoard()
    clickLocation = templateMatch("bots/myHospital/screenshot/billboard-screen.png" , "bots/myHospital/template/billboard-sample2.png")
    adbTapScreen(clickLocation)

    #wait for box
    time.sleep(5)

    #clickok
    clickLocation = (1480, 1116)
    adbTapScreen(clickLocation)

    #watch ad
    time.sleep(60)
    #35

    #close ad
    clickLocation = (2668, 80)
    adbTapScreen(clickLocation)

    #wait for ad to close
    time.sleep(5)

    #check if the claim button is visable
    pullImage()
    #clickLocation = findBillBoardReward()
    clickLocation = templateMatch("bots/myHospital/screenshot/billboard-screen.png" , "bots/myHospital/template/claimReward3.png")
    adbTapScreen(clickLocation)

getReward()