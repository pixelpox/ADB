import cv2
import numpy as np


def test():
    
    img = cv2.imread("bots/myHospital/screenshot/billboard-screen-no-reward.png")
    #img = cv2.imread("bots/myHospital/screenshot/billboard-screen-with-reward.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread("bots/myHospital/template/billboard-sample2.png" , cv2.IMREAD_GRAYSCALE)
    cv2.imshow("template" , template)

    w, h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(result >= 0.9)
    #print(loc)

    clickLocation = ()


    #check if there is any results if not return
    if not loc[0].size and not loc[1].size:
        #print("list is empty")
        return clickLocation

    for pt in zip(*loc[::-1]):
        #print(pt)
        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
        clickLocation = (int(pt[0]+(w/2)), int(pt[1]+(h/2)))
        cv2.circle(img, clickLocation, 10, (255, 0, 0), -1)

    #cv2.imshow("img", img)
    #cv2.imshow("result" , result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return clickLocation


clickLocation = test()

if clickLocation:
    print(clickLocation)
else:
    print("no match found boss")
