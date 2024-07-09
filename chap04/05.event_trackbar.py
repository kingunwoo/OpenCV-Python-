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
cv2.waitKey(0)
cv2.destroyAllWindows()