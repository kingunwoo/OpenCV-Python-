import numpy as np
import cv2

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)         
img = np.full((300, 500, 3), white, np.uint8)             # 컬러 영상 생성 및 초기화

center = (img.shape[1]//2, img.shape[0]//2)         		# 영상의 중심 좌표
pt1, pt2 = (300, 50), (100, 220)
shade = (pt2[0] + 2, pt2[1] + 2)                          # 그림자 좌표

cv2.circle(img, center, 100, blue)                         # 원 그리기 
cv2.circle(img, pt1   , 50 , orange, 2)
cv2.circle(img, pt2   , 70 , cyan  , -1)                   # 원 내부 채움

font = cv2.FONT_HERSHEY_COMPLEX;
cv2.putText(img, "center_blue", center, font, 1.0, blue)
cv2.putText(img, "pt1_orange", pt1, font, 0.8, orange)
cv2.putText(img, "pt2_cyan",   shade, font, 1.2, black, 2)   # 그림자 효과
cv2.putText(img, "pt2_cyan",   pt2, font, 1.2, cyan , 1)

title = "Draw circles"
cv2.namedWindow(title)
cv2.imshow(title, img)
cv2.waitKey(0)