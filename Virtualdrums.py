import cv2 as cv
import numpy as np
import pyautogui
import imutils

def press(key):
    pyautogui.press(key)

cap = cv.VideoCapture(1)

while True:
    _, frame = cap.read()
    frame = cv.flip(frame,1)
    frame = imutils.resize(frame, height=700, width=900)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    lowred = np.array([131,90,106])
    highred = np.array([255, 255, 255])
    lowblue = np.array([90, 120, 0])
    highblue = np.array([150, 255, 255])

    red_mask = cv.inRange(hsv, lowred, highred)
    blue_mask = cv.inRange(hsv, lowblue, highblue)
    # blue rectangle test(top-left corner of the screen) 
    # image/frame, startpoint, endpoint, color, thickness
    cv.rectangle(frame, (0,0), (200,150), (255,0,0),1)
    cv.putText(frame,'Ride',(70,80),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (210,0), (430,150), (0,0,255),1)
    cv.putText(frame,'Ride bell',(245,80),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)
    cv.rectangle(frame, (440,0), (650,150), (255,0,0),1)
    cv.putText(frame,'Hithat ped',(445,80),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (660,0), (900,150), (0,0,255),1)
    cv.putText(frame,'Crash',(730,80),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)


    cv.rectangle(frame, (0,160), (50,370), (255,0,0),1)
    cv.putText(frame,'Snare',(10,290),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (0,380), (50,570), (0,0,255),1)
    cv.putText(frame,'Snare rim',(10,500),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)
    
    cv.rectangle(frame, (850,160), (900,370), (255,0,0),1)
    cv.putText(frame,'Hithat',(770,290),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (850,380), (900,570), (0,0,255),1)
    cv.putText(frame,'Hithat open',(670,500),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)


    cv.rectangle(frame, (0,580), (200,700), (255,0,0),1)
    cv.putText(frame,'Tom-high',(50,640),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (210,580), (430,700), (0,0,255),1)
    cv.putText(frame,'Tom-mid',(250,640),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)
    cv.rectangle(frame, (440,580), (650,700), (255,0,0),1)
    cv.putText(frame,'Tom-low',(480,640),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv.LINE_AA)
    cv.rectangle(frame, (660,580), (900,700), (0,0,255),1)
    cv.putText(frame,'Hihat open',(740,640),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv.LINE_AA)

    #For red object
    contours, hierachy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted( contours, key=lambda x: cv.contourArea(x), reverse= True)

    for cnt in contours:
        (x,y,h,w) = cv.boundingRect(cnt)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # print(x,y)
        break
    # #For blue object
    contours, hierachy = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted( contours, key=lambda x: cv.contourArea(x), reverse= True)

    for cnt in contours:
        (x,y,h,w) = cv.boundingRect(cnt)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # print(x,y)
        # for all the keys
        if x > 0 and y > 0 and x < 200 and y < 150:
            press('7') #RIDE
            break      
        if x > 210 and y > 0  and x < 430 and y < 150:
            press('8') #RIDE BELL
            break      
        if x > 440 and y > 0 and x < 650 and y < 150:
            press('6') #HIT HAT CLOSE
            break      
        if x > 660 and y > 0 and x < 900 and y < 150:
            press('9') #CRASH
            break      
        
        
        if x > 0 and y > 160 and x < 50 and y < 370:
            press('2') #SNARE
            break      
        if x > 0 and y > 380 and x < 50 and y < 570:
            press('3') #SNARE RIM
            break      
        if x > 850 and y > 160 and x < 900 and y < 370:
            press('4') #HIT HAT 
            break      
        if x > 850 and y > 380 and x < 900 and y < 570:
            press('5') #HIT HAT OPEN 
            break      
        
        
        if x > 0 and y > 580 and x < 200 and y < 700:
            press('q') #TOM HI
            break      
        if x > 210 and y > 580 and x < 430 and y < 700:
            press('w') #TOM MID
            break      
        if x > 440 and y > 580 and x < 650 and x < 700:
            press('e') #TOM LOW 
            break      
        if x > 660 and y > 580 and x < 900 and y < 700:
            press('1') #HIT HAT OPEN 
            break              
        break

    cv.imshow("frame", frame)

    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()
