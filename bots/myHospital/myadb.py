import sys
import os
from shutil import copyfile
import time



def sendBackKey():
    cmd = 'adb shell input keyevent 4'
    os.system(cmd)

    return True