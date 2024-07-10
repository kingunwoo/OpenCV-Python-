import cv2

image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap04/images/matplot.jpg", cv2.IMREAD_GRAYSCALE)

if image is None :
    raise Exception("영상 파일 읽기 에러")

cv2.imshow('test', image)

cv2.imwrite("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap04/images/testJ.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap04/images/testJ.png", image, (cv2.IMWRITE_PNG_COMPRESSION, 9))

cv2.waitKey(0)