import numpy as np
import cv2

mat1 = np.zeros((600, 400,3),  np.uint8)

title1 = 'title1'

cv2.namedWindow(title1)

cv2.rectangle(mat1, (100,100), (300,400),(0,0,255),2)


cv2.imshow(title1, mat1)
cv2.waitKey(0)
cv2.destroyAllWindows()

