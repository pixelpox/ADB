import cv2
import numpy as np

def findBillBoard():
    img = cv2.imread("bots/myHospital/screenshot/billboard-screen.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread("bots/myHospital/template/billboard-sample2.png", cv2.IMREAD_GRAYSCALE)

    w, h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(result >= 0.9)
    #print(loc)

    for pt in zip(*loc[::-1]):
        #print(pt)
        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
        clickLocation = (int(pt[0]+(w/2)), int(pt[1]+(h/2)))
        cv2.circle(img, clickLocation, 10, (255, 0, 0), -1)


    return clickLocation

def findBillBoardReward():
    img = cv2.imread("bots/myHospital/screenshot/billboard-screen.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread("bots/myHospital/template/claimReward3.png", cv2.IMREAD_GRAYSCALE)

    w, h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(result >= 0.9)
    #print(loc)

    for pt in zip(*loc[::-1]):
        #print(pt)
        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
        clickLocation = (int(pt[0]+(w/2)), int(pt[1]+(h/2)))
        cv2.circle(img, clickLocation, 10, (255, 0, 0), -1)


    return clickLocation