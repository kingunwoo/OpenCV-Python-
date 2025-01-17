import numpy as np
import cv2

img = np.zeros((300,400,3), np.uint8)
img[:] = 200  
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)

def OnMouse(event, x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x,y), 20, (255,0,0))
        cv2.imshow(title1,img)        
        
    elif(event == cv2.EVENT_RBUTTONDOWN):
        cv2.rectangle(img, (x,y), (x+30,y+30),(0,255,0),2)
        cv2.imshow(title1,img)
        

cv2.setMouseCallback(title1,OnMouse)
cv2.imshow(title1,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
