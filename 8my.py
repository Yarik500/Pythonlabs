import numpy as np
import cv2 as cv
from math import sqrt
#1================================================

img_1 = cv.imread('./Lab-8/images/variant-7.jpg')
img_flip = cv.flip(img_1,0)
img_flip = cv.flip(img_flip,-1)
cv.imshow('Flipped',img_flip)
cv.imshow('Orig',img_1)
#2================================================


params=[20,40,60,80,100]
cap = cv.VideoCapture(0)
ret,frame = cap.read()
dimensions = frame.shape
print(dimensions)
x, y, w, h =0, 0, dimensions[1], dimensions[0] # simply hardcoded the values
track_window = (x, y, w, h)
center_x= w//2
center_y= h//2
print(w,h,center_x,center_y)
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((30., 30.,30.)), np.array((255.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.medianBlur(frame,5)
        frame = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
        cimg = cv.cvtColor(frame,cv.COLOR_GRAY2BGR)
        cv.circle(cimg,(center_x,center_y),2,(0,0,255),3)
        for i in params:
            circles = cv.HoughCircles(frame,cv.HOUGH_GRADIENT,1,20,param1=50,param2=i,minRadius=0,maxRadius=100)
            if type(circles)!=type(None): 
                if len(circles[0])==1:
                    circles = np.uint16(np.around(circles))
                    for i in circles[0,:]:
                        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
                        
                        cv.putText(cimg, str(round(sqrt((i[0]-center_x)**2+(i[1]-center_y)**2))), (300, 100),
                                          cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    break
            else:
                pass
        cv.imshow('frame',cimg)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
         break