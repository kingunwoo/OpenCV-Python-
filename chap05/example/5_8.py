import numpy as np, cv2

img  = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap05/images/color.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if  img is None: raise Exception("영상 파일 읽기 오류 ")

mask = np.zeros(img.shape[:2], dtype = np.uint8)
center = (190,170)
black_pannel = np.zeros(img.shape, dtype = np.uint8)
print(img.shape)
print(black_pannel.shape)

cv2.ellipse(black_pannel, center, (150,100),  0, 0, 360, (255,255,255), -1)     

merged_img = cv2.bitwise_and(black_pannel, img)
cv2.imshow('masked',merged_img)
cv2.waitKey()