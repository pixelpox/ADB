import datetime
from datetime import timedelta
from collectVitamins import collectVitamins
import time

vitaminlastCheck = datetime.datetime.now()
vitaminwaitPeriod = timedelta(minutes=1)
#vitaminwaitPeriod = timedelta(minutes=12)
vitaminnextCheck = (vitaminlastCheck + vitaminwaitPeriod)


def setupVitamins():
    print("setup vitamins")
    collectVitamins()

    #set last check to now
    global vitaminlastCheck
    vitaminlastCheck = datetime.datetime.now()

    #calculate the next check
    global vitaminnextCheck
    vitaminnextCheck = (vitaminlastCheck + vitaminwaitPeriod)

    print("setup vitamins Complete")

    return True


def checkVitamins():
    print("time to check the vitamins")
    global vitaminnextCheck
    global vitaminlastCheck


    currentTime = datetime.datetime.now()

    if currentTime > vitaminnextCheck:
        print("time to check")
        collectVitamins()
        vitaminlastCheck = datetime.datetime.now()
        vitaminnextCheck = (vitaminlastCheck + vitaminwaitPeriod)
    else:
        print("The next check will be: ", vitaminnextCheck)

    print("finished")
    return True


setupVitamins()

while(True):
    checkVitamins()
    time.sleep(5)