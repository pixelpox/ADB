import sys
import os
from shutil import copyfile
import time



def pullImage(logScreenshot = True):

    capCmd = 'adb shell screencap -p /sdcard/ADBScreenshot.png'
    #pullCmd = 'adb pull /sdcard/billboard-screen.png screenshot/ >/dev/null 2>&1'
    pullCmd = 'adb pull /sdcard/ADBScreenshot.png screenshot/'
    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")

   


    print("Capuring screen")
    os.system(capCmd)
    print("Pulling image")
    os.system(pullCmd)
    
    #copy image
    if(logScreenshot):
        copyfile('screenshot/ADBScreenshot.png' , 'screenshot/log/ADBScreenshot_'+timestr+'.png')

    return