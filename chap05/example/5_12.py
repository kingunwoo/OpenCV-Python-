import numpy as np, cv2

image  = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap05/images/color.jpg", cv2.IMREAD_COLOR) 
gray_image  = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap05/images/color.jpg", cv2.IMREAD_GRAYSCALE)  # 로고 영상 읽기
if  image is None: raise Exception("영상 파일 읽기 오류 ")

mask1 = np.zeros(image.shape, dtype = np.uint8)
cv2.ellipse(mask1, (100,100), (50,50),  0, 0, 360, (50,50,50), -1)
light_up = cv2.add(mask1,image)

mask2 = np.zeros(image.shape[:2], dtype = np.uint8)
cv2.ellipse(mask2, (200,200), (150,50),  0, 0, 360, (50,50,50), -1)
print(gray_image.shape)
(min_val, max_val, _, _) = cv2.minMaxLoc(gray_image,mask2)  # 최솟값과 최댓값 가져오기
ratio = 255/(max_val - min_val)
edit_img = cv2.subtract(image,min_val,mask=mask2)
#(image - min_val) * ratio
dst = np.round(edit_img * ratio).astype('uint8')

total_image = cv2.add(edit_img,light_up)


cv2.imshow("dst_3"  , total_image)
cv2.waitKey(0)
     