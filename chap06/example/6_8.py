import numpy as np, cv2

image1 = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/add1.jpg", cv2.IMREAD_COLOR)  
image2 = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/add2.jpg", cv2.IMREAD_COLOR)
if image1 is None or image2 is None: raise Exception("read_error")

add_image = cv2.addWeighted(image1,0.5,image2,0.5,0)

cv2.imshow("add_image", add_image)
cv2.waitKey(0)
cv2.destroyAllWindows()