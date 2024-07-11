import numpy as np, cv2

pts1 = np.array([(200, 50, 1), (400, 50, 1),
                                (400, 250, 1), (200, 250, 1)], np.float32)

theta = 45 * np.pi / 180
m = np.array([ [np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [ 0,0,1]], np.float32)

delta = (pts1[2] - pts1[0]) // 2
center = pts1[0] + delta

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)
t1[2] = (-center[0], -center[1], 1)
t2[2] = (center[0], center[1], 1)


pts2 = np.dot(pts1,t1)
pts2 = np.dot(pts2, m)
pts2 = np.dot(pts2, t2)
print(center)

image = np.full((400,500,3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts2[:, :2])], True, (0,0,255), 2)
cv2.polylines(image, [np.int32(pts1[:, :2])], True, (255,0,0), 3)
cv2.imshow("image", image)
cv2.waitKey(0)
    
