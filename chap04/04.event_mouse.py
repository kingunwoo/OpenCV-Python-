import numpy as np
import cv2

img = np.zeros((200,300), np.float16)
img[:] = 200
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)

def OnMouse(event, x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONUP):
        print("마우스 왼쪽 떼기")
    elif(event == cv2.EVENT_LBUTTONDOWN):
        print("left down")
    elif(event == cv2.EVENT_RBUTTONDOWN):
        print("right down")
    elif(event == cv2.EVENT_RBUTTONUP):
        print("right up")
    elif(event == cv2.EVENT_LBUTTONDBLCLK):
        print("left double click")        

cv2.setMouseCallback(title1,OnMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
