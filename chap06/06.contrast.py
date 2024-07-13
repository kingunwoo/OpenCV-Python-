import numpy as np, cv2

image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/contrast.jpg", cv2.IMREAD_GRAYSCALE)  

avg = np.mean(image) / 2


dst1 =cv2.addWeighted(image,0.5,0,0,avg)
dst2 =cv2.addWeighted(image,2,0,0,-avg)
dst3 =cv2.addWeighted(image,0.5,0,0,0)
dst4 =cv2.addWeighted(image,2,0,0,0)
print(avg)

cv2.imshow("img", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)

cv2.waitKey(0)


