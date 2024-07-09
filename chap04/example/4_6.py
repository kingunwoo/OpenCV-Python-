import numpy as np
import cv2

img = np.zeros((300,400), np.uint8)
img[:] = 100

title = '4_6'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.moveWindow(title, 600, 500)
cv2.imshow(title, img)

cv2.waitKey(0)
cv2.destroyAllWindows()