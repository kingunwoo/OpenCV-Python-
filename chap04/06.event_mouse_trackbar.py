import numpy as np
import cv2

def onChange(value):
    img[:] = value
    cv2.imshow(title1,img)
    
def OnMouse(event, x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        img[:] = img[:] - 10
        cv2.setTrackbarPos('Bright', title1, img[0][0])
        cv2.imshow(title1, img)
        
    elif(event == cv2.EVENT_RBUTTONDOWN):
        img[:] = img[:] + 10
        cv2.setTrackbarPos('Bright', title1, img[0][0])
        cv2.imshow(title1, img)
        
img = np.zeros((300,500), np.uint8)
img[:] = 20
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(title1,img)

cv2.createTrackbar('Bright', title1, img[0][0], 255, onChange)
cv2.setMouseCallback(title1,OnMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()