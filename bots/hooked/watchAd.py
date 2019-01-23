import cv2
import numpy as np
import time
import os
import threading

myTemplate = 'template/watchAdButtonSmall2.png'
myTemplate2 = ('template/watchAdButtonSmall2.png' , 'template/exitAdButton.png')

def watchAd(clickLocation):
    print("watching the ad")



def adbTapScreen(clickLocation):
    print("Im about to tap the screen")
    #print(clickLocation[0])
    #print(clickLocation[1])
    
    tapCmd = "adb shell input tap " + str(clickLocation[0]) + " " + str(clickLocation[1])
    
    #print(tapCmd)
    os.system(tapCmd)

def show_webcam(mirror=False , resize = False , accuracy = 0.8):
    cam = cv2.VideoCapture('http://127.0.0.1:55932/device/ce031713383080fa0c/video.flv')
    while True:
        ret_val, img = cam.read()

        #image processing
        if mirror: 
            img = cv2.flip(img, 1)

        if resize:
            img = cv2.resize(img , (1440,2960))

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       
        template = cv2.imread('template/watchAdButtonSmall2.png' , cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
    
        #comapre images
        result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
        #cv2.imshow("result" , result)
        #cv2.imshow('my webcam', gray_img)

        #matches that are over threshhold
        loc = np.where(result >= accuracy)

        clickLocation = ()


    

        for pt in zip(*loc[::-1]):
            #print(pt)
            cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
            clickLocation = (int(pt[0]+(w/2)), int(pt[1]+(h/2)))
            cv2.circle(img, clickLocation, 10, (255, 0, 0), -1)








        preview = img

        if resize:
            preview = cv2.resize(preview , (352,736))

        cv2.imshow('my webcam', preview)

        #check if there is any results if not return
        if not loc[0].size and not loc[1].size:
            print("list is empty")
            #return clickLocation
        else:
            print('TAP TAP TAP')

            if not resize:
                clickLocation = (clickLocation[0]*4 , clickLocation[1]*4 )


            print("x:" + str(clickLocation[0]) + " Y:" + str(clickLocation[1]))

            threading.Thread(target=adbTapScreen(clickLocation)).start
            #adbTapScreen(clickLocation)
            time.sleep(5)
            cam = cv2.VideoCapture('http://127.0.0.1:55932/device/ce031713383080fa0c/video.flv')







        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=False)


if __name__ == '__main__':
    main()
    
    
