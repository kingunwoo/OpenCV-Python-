import numpy as np
import cv2

red, blue = (0, 0, 255), (255, 0, 0)    
img = np.full((400, 600, 3), (255,255,255), np.uint8)           

center = (300,200)  #biggest radius == 50         		
title = "Draw TG"
cv2.namedWindow(title)


cv2.circle(img, center, 100, blue,-1)
cv2.ellipse(img, center, (100,100),  0,-180, 0, red, -1)
cv2.ellipse(img, (250,200), (50,50),  0,0,180, red, -1)
cv2.ellipse(img, (350,200), (50,50),  0,-180, 0, blue, -1)    
cv2.imshow(title, img)

cv2.waitKey(0)