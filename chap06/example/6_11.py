import numpy as np,cv2

def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels) > 1 else (bsize[0], 1) #bsize == count of bins ex)67
    hist = np.zeros(shape, dtype=np.int32)  
    gap = np.divide(ranges[1::2], bsize)  

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap).astype(np.uint8) 
            hist[tuple(idx)] += 1  
    return hist


image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap06/images/pixel.jpg", cv2.IMREAD_COLOR)  
channels = [0, 1, 2] 
bsize = (8, 8, 8)  
ranges = [0, 256, 0, 256, 0, 256]  

hist = calc_histo(image, channels, bsize, ranges)
print(hist)
