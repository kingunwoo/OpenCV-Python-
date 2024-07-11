import numpy as np, cv2

logo  = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap05/images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if  logo is None: raise Exception("영상 파일 읽기 오류 ")

blue, green, red = cv2.split(logo)



masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
masks = cv2.split(masks) 

b1 = np.zeros(masks[0].shape, dtype = np.uint8)
b2 = np.zeros(b1.shape, dtype = np.uint8)

logo_blue = cv2.merge((blue,b1,b2))    
logo_red = cv2.merge((b1,b2,red))    
logo_green = cv2.merge((b1,green,b2))    


cv2.imshow("logo", logo)
cv2.imshow("logo_blue", logo_blue)
cv2.imshow("logo_red", logo_red)
cv2.imshow("logo_green", logo_green)
cv2.waitKey()