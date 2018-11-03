import sys
import subprocess
import os


def adbTapScreen(clickLocation):
    print("Im about to tap the screen")
    print(clickLocation[0])
    print(clickLocation[1])
    
    tapCmd = "adb shell input tap " + str(clickLocation[0]) + " " + str(clickLocation[1])
    
    print(tapCmd)
    os.system(tapCmd)