import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)    	
img = np.zeros((400, 600, 3), np.uint8)    					
img[:] = (255, 255, 255)

pt1, pt2 = (50, 50), (250, 150)                   		        
pt3, pt4 = (400, 150), (500,  50)
roi = 50, 200, 200, 100

cv2.line(img, pt1, pt2, blue)
cv2.line(img, pt3, pt4, green, 3, cv2.LINE_AA)

cv2.rectangle(img, pt1, pt2, red, 3, cv2.LINE_4)
cv2.rectangle(img, roi, red, 3, cv2.LINE_8)

cv2.imshow('Line & Rectangle', img)							
cv2.waitKey(0)
cv2.destroyAllWindows()											