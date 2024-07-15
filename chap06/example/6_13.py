import numpy as np
import cv2

def change(image,mode):
    if(mode == 'rgb_to_ycbcr'):
        b,g,r = cv2.split(image)
        converted_image_y = np.zeros_like(b,dtype= np.float32)
        converted_image_cb = np.zeros_like(b,dtype= np.float32)
        converted_image_cr = np.zeros_like(b,dtype= np.float32)
        converted_image_y = ((0.299*r) + (0.587 * g) + (0.114 *b)).astype(np.uint8)
        converted_image_cb = ((r - converted_image_y)*0.564 +128).astype(np.uint8)
        converted_image_cr = ((b - converted_image_y)*0.713 +128).astype(np.uint8)
        converted_image = cv2.merge((converted_image_y,converted_image_cb,converted_image_cr))
        return converted_image


image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/pixel.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
if image is None: raise Exception("image error")

cvt_img = change(image,'rgb_to_ycbcr')
cv2.imshow('show', image)
cv2.imshow("cvt_img", cvt_img)
cv2.waitKey(0)