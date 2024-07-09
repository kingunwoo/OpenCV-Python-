import numpy as np
import cv2

img = np.zeros((300,500), np.uint8)
img[:]  = 0

title1, title2 = 'title1', 'title2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1,50,50)
cv2.moveWindow(title2,150,150)

cv2.imshow(title1, img)
cv2.imshow(title2,img)

cv2.waitKey(0)
cv2.destroyAllWindows()

