import numpy as np
import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#hsv = h 0~179, s 0~255, v 0~255

def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels) > 1 else (bsize[0], 1) #bsize == count of bins ex)67
    hist = np.zeros(shape, dtype=np.int32)  
    gap = np.divide(ranges[1::2], bsize)  

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap).astype(np.uint8) 
            hist[tuple(idx)] += 1  
    return hist

bgr_img = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/pixel.jpg", cv2.IMREAD_COLOR) 
if bgr_img is None: raise Exception("read_error") 
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

channels = [0, 1] 
bsize = (7,30)  
ranges = [0, 180, 0, 256]  

hist = calc_histo(hsv_img, channels, bsize, ranges)
print(hist)

plt.imshow(hist, interpolation='nearest')
plt.title('2D Histogram for Hue and Saturation')
plt.xlabel('Hue')
plt.ylabel('Saturation')
plt.colorbar()
plt.show()