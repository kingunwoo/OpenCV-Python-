import numpy as np, cv2
import matplotlib.pyplot as plt

def draw_histo(hist, shape=(1000, 1280)):
    hist_img = np.full( shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]             # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                         # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 150, -1)
        cv2.rectangle(hist_img, roi, 0, 1)

    return   cv2.flip(hist_img, 0)                        # 영상 상하 뒤집기 후 반환

image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/hue_hist.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("read_error")

reduce_sum_y = cv2.reduce(image,dim = 1, rtype = cv2.REDUCE_SUM, dtype=cv2.CV_32S)
reduce_sum_x = cv2.reduce(image,dim = 0, rtype = cv2.REDUCE_SUM, dtype=cv2.CV_32S)
