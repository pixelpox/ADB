import sys
import os


def pullImage():

    capCmd = 'adb shell screencap -p /sdcard/billboard-screen.png'
    #pullCmd = 'adb pull /sdcard/billboard-screen.png screenshot/ >/dev/null 2>&1'
    pullCmd = 'adb pull /sdcard/billboard-screen.png bots/myHospital/screenshot/'


    print("Capuring screen")
    os.system(capCmd)
    print("Pulling image")
    os.system(pullCmd)