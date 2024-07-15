import numpy as np
import cv2

image1 = np.arange(50 * 512, dtype = np.float32)
image1 = image1.reshape((50,512))

print(image1.shape)

rows = image1.shape[0]
cols = image1.shape[1]

for i in range(rows):
    for j in range(cols):
        image1[i][j] = 255 -(j/512*255)
        
        
image1 = image1.astype(np.uint8)
cv2.imshow("image1", image1)
#cv2.imshow("image2", image2)
cv2.waitKey(0)