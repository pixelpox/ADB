import os
import time
import subprocess
from pullImage import pullImage
from findImage import templateMatch
from clicker import adbTapScreen

def myinit():
    subprocess.Popen('powershell.exe adb shell monkey -p com.cherrypickgames.myhospital -v 500')
    #use the following to see if the game is running... wont work if its in the background
    #adb shell pidof com.cherrypickgames.myhospital
    #use the following to seee what has the current focus
    #adb shell dumpsys window windows | select-string -Pattern 'mCurrentFocus'


def watchAdvertisement():
    time.sleep(15)
    print("watching ad")

    clickLocation = ()

    while(not clickLocation):
        print("attempting to find close button on ad")
        pullImage()
        clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/closeAdButton.png")
        print(clickLocation)
        time.sleep(5)
        
    
    print("found it! clicking it")
    adbTapScreen(clickLocation)
    
    #wait for ad to close
    time.sleep(5)


#rewards
def getReward():
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/billboard-sample2.png")
    if(not clickLocation):
        clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/billboardNoReward.png")
        print("I have to wait for more rewards")
        return False


    
    adbTapScreen(clickLocation)

    #wait for box
    time.sleep(5)

    #clickok
    clickLocation = (1480, 1116)
    adbTapScreen(clickLocation)

    #watch ad
    watchAdvertisement()
 
    #check if the claim button is visable
    pullImage()
    #clickLocation = findBillBoardReward()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/claimReward3.png")
    adbTapScreen(clickLocation)

    return True


while(True):
    gotReward = getReward()
    
    if(gotReward):
        time.sleep(5)
    else:
        print("maybe I'll try in a minute")
        time.sleep(60)