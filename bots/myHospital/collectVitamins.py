import os
import time
import subprocess
from pullImage import pullImage
from findImage import templateMatch
from clicker import adbTapScreen


def collectVitamins():
    print("lets collect some vitamins")
    
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/dummy.png")
    if(clickLocation):
        adbTapScreen(clickLocation)
        #wait for box
        time.sleep(5)
    
    #check if the maternity report has popped up
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/maternityReport.png")
    if(clickLocation):
        print("I can see the maternity report")
        clickLocation = (1480 , 1248)
        adbTapScreen(clickLocation)
        #wait for maternity centre to load
        time.sleep(20)

    #find the vitamins button
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/vitaminButton.png")
    if(clickLocation):
        adbTapScreen(clickLocation)
        #wait for pop up
        time.sleep(5)

    #click the storage button, loop if there is more then one
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/vitaminStorageButton.png")
    print(clickLocation)
    if(not clickLocation):
        print("STORAGE BUTTON: I cant see anything")
        return
    while(clickLocation):
        print("I see a box")
        adbTapScreen(clickLocation)
        #wait for animation to play
        time.sleep(2)
        pullImage()
        clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/vitaminStorageButton.png")

    #close the vitamin box
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/closeButton.png")
    adbTapScreen(clickLocation)

    #wait for box to close
    time.sleep(5)

    #Go home
    pullImage()
    clickLocation = templateMatch("bots/myHospital/screenshot/ADBScreenshot.png" , "bots/myHospital/template/homeButton.png")
    adbTapScreen(clickLocation)

    return True

collectVitamins()
