import numpy as np, cv2

image1 = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/add1.jpg", cv2.IMREAD_COLOR)  
image2 = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/add2.jpg", cv2.IMREAD_COLOR)
if image1 is None or image2 is None: raise Exception("read_error")

value1 = 50
value2 = 50

title = 'title'

def onChange_image1(value):
    value1 = value
    add_image = cv2.addWeighted(image1, (value1/100), image2, (value2/100), 0)
    cv2.imshow(title,add_image)
    
def onChange_image2(value):
    value2 = value
    add_image = cv2.addWeighted(image1, (value1/100), image2, (value2/100), 0)
    cv2.imshow(title,add_image)

add_image = cv2.addWeighted(image1, (value1/100), image2, (value2/100), 0)

cv2.imshow(title, add_image)    
cv2.createTrackbar('image1', title, value1, 100, onChange_image1)
cv2.createTrackbar('image2', title, value2, 100, onChange_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()