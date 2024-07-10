import numpy as np
import cv2

img = np.zeros((300,400,3), np.uint8)
img[:] = 200  
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)
global radius, thick

def onChange_radius(value):
    global radius
    radius = value

def onChange_thick(value):
    global thick
    thick = value


def OnMouse(event, x,y,flags,param):
    global radius, thick
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x,y), radius, (255,0,0))
        cv2.imshow(title1,img)        
        
    elif(event == cv2.EVENT_RBUTTONDOWN):
        cv2.rectangle(img, (x,y), (x+30,y+30),(0,255,0),thick)
        cv2.imshow(title1,img)
        
    elif(event == cv2.EVENT_FLAG_MBUTTON):
        #what is wheelbutton
        cv2.ellipse(img, (x,y), (100,50),  0, 0, 360, (0,0,255), 1)     
        cv2.imshow(title1,img)
        

cv2.setMouseCallback(title1,OnMouse)
cv2.createTrackbar('thick', title1, 5, 255, onChange_thick)
cv2.createTrackbar('radius', title1, 20, 255, onChange_radius)
cv2.imshow(title1,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
