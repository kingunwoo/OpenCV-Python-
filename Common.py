import numpy as np
import cv2

def filter_convolution_2d(image, filter):
    h = image.shape[0]
    w = image.shape[1]
    fh = filter.shape[0]
    fw = filter.shape[1]
    oh = (h -fh+1)
    ow = (w -fw+1)

    im2col = np.zeros((oh*ow,fh*fw))
    count = 0
    for row in range(oh):
        for col in range(ow):
            patch = image[row:row+fh,col:col+fw].flatten()
            im2col[count,:] = patch
            count +=1
    filter = filter.flatten().T
    conv_result = np.dot(im2col, filter)
    conv_result = np.clip(conv_result, 0, 255)
    conv_result = conv_result.reshape(oh,ow)
    return(conv_result)

