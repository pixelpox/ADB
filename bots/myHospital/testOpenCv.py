from findImage import templateMatch
from pullImage import pullImage
import time

#templateMatch("bots/myHospital/screenshot/billboard-screen.png" , "bots/myHospital/template/closeAdButton.png" , 0.8 , True)
def whileTest():
    clickLocation = ()

    while(not clickLocation):
        print("attempting to find close button on ad")
        clickLocation = templateMatch("bots/myHospital/screenshot/maternityReportScreenshot.png" , "bots/myHospital/template/closeButton.png" , 0.9 , True)
        print(clickLocation)
        time.sleep(5)
    
    print("found it! clicking it")
    return



def simpleTest(sourcePath , templatePath):
    clickLocation = templateMatch(sourcePath , templatePath  , 0.9 , False)
    
    print(clickLocation)
    return

#find Vitaminbutton on maternity centre screen
#simpleTest("bots/myHospital/screenshot/maternityCentre.png" , "bots/myHospital/template/vitaminButton.png")

#click vitamin storage button
simpleTest("bots/myHospital/screenshot/vitaminScreenshot.png" , "bots/myHospital/template/vitaminStorageButton.png")