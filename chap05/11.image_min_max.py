import numpy as np, cv2

image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap05/images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

(min_val, max_val, _, _) = cv2.minMaxLoc(image)  # 최솟값과 최댓값 가져오기

ratio = 255/(max_val - min_val)
dst_1 = np.round((image - min_val) * 0.2).astype('uint8')
dst_2 = np.round((image - min_val) * 6).astype('uint8')
dst_3 = np.round((image - min_val) * ratio).astype('uint8')
(min_dst, max_dst, _, _) = cv2.minMaxLoc(dst_3)

print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
cv2.imshow("image", image)
cv2.imshow("dst_1"  , dst_1)
cv2.imshow("dst_2"  , dst_2)
cv2.imshow("dst_3"  , dst_3)
cv2.waitKey(0)