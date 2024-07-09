import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title
    col = (255,0,0)
    pt = (x, y)
    if (event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(image, pt, 100, col, 5,1)
    elif(event == cv2.EVENT_RBUTTONDOWN):
        cv2.rectangle(image, pt, pt+(30,30), col, 2)
    
    cv2.imshow(title, image)
        
image = np.ones((300,300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()