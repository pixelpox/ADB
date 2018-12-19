import os
import time
import subprocess
from pullImage import pullImage
from findImage import templateMatch
from clicker import adbTapScreen
from myadb import sendBackKey

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

    attempt = 0
    foundCloseButton = True

    while(not clickLocation):
        attempt += 1
        print("attempting to find close button on ad")
        pullImage()
        clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/closeAdButton.png")
        print(clickLocation)
        time.sleep(5)

        if(attempt > 5):
            print("trying to escape")
            foundCloseButton = False
            sendBackKey()
            break


    if(foundCloseButton):
        print("found it! clicking it")
        adbTapScreen(clickLocation)
    
    #wait for ad to close
    time.sleep(5)


#rewards
def getReward():
    pullImage()
    clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/billboard-sample2.png")

    #If that didnt work look for heart billboard
    if(not clickLocation):
        clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/heartbillboard.png")


    if(not clickLocation):
        clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/billboardNoReward.png")
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
    clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/claimReward3.png")
    adbTapScreen(clickLocation)

    return True

attempt = 0
while(True):
    
    gotReward = getReward()
    
    if(gotReward):
        #reset attempt counter
        attempt = 0
        time.sleep(5)

    else:
        attempt += 1
        print("maybe I'll try in a minute")
        time.sleep(2)
        #time.sleep(60)

        if(attempt > 5):
            print("something is wrong with the board or i cant see it")
            print("Try to click the inactive board")
            #look for the switched off billboard
            clickLocation = templateMatch("screenshot/ADBScreenshot.png" , "template/billboardNoReward.png")
            if(not clickLocation):
                print("I give up!")
                exit
            
            #The billboard is switched off, see if I have hit the max limit
            adbTapScreen(clickLocation)
            pullImage()

            #check the image
            #if it says max reached then quit

            #if it says wait for more ads reset counter to zero and go around again


