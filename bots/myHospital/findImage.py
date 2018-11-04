import cv2
import numpy as np

def templateMatch(sourcePath , templatePath , accuracy = 0.9 , showImage = False):
    img = cv2.imread(sourcePath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(templatePath , cv2.IMREAD_GRAYSCALE)
    cv2.imshow("template" , template)

    #get x and y of the template
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(result >= accuracy)


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

    if showImage:
        
        
        imgResize = cv2.resize(img , (1600,900))
        cv2.imshow("img", img)
        cv2.imshow("img2", imgResize)

        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 600,600)
        cv2.imshow("result" , result)
        

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return clickLocation

def messabout():
    clickLocation = False
    #clickLocation = test()

    if clickLocation:
        print(clickLocation)
    else:
        print("no match found boss")
