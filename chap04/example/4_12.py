import numpy as np
import cv2

def onChange(value):
    img[:] = value
    cv2.imshow(title1,img)

img = np.zeros((300,500), np.uint8)
img[:] = 200
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(title1,img)

cv2.createTrackbar('Bright', title1, img[0][0], 255, onChange)

while(True):
    key = cv2.waitKeyEx(0)
    
    if(key == 27):
        break
    
    elif(key == 65363):
        cv2.setTrackbarPos('Bright', title1, img[0][0]+30)
    elif(key == 65361):
        cv2.setTrackbarPos('Bright', title1, img[0][0]-30)
    else:
        print(key)

cv2.destroyAllWindows()