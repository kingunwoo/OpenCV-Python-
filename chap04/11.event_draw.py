import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255,255,255) 
#img = np.zeros((300,400), np.float16)
#img[:] = 0
img = np.full((400, 500, 3), white, np.uint8)

global Rec1, Rec2, Cir1, Cir2 
Rec1, Cir1 = -1, -1

title = "title"
cv2.namedWindow(title,cv2.WINDOW_AUTOSIZE)

def OnMouse(event, x, y,flags,param):
    global Rec1, Rec2, Cir1, Cir2 
    
    if(event == cv2.EVENT_LBUTTONDOWN):
        if(Rec1 == -1):
            Rec1 = (x, y)
            print("rectangle_1_is_choosen")
        elif(Rec1 != -1):
            Rec2 = (x, y)
            cv2.rectangle(img, Rec1, Rec2, blue, 3, cv2.LINE_4)
            cv2.imshow(title, img)
            print("rectangle_is_finish")
            Rec1 = -1
            
    elif(event == cv2.EVENT_RBUTTONDOWN):
        if(Cir1 == -1):
            Cir1 = (x, y)
            print("circle_center_is_choosen")
        elif(Cir1 != -1):
            Cir2 = (x, y)
            radius = np.sqrt((Cir2[0]-Cir1[0])**2 + (Cir2[1]-Cir1[1])**2)
            print(radius)
            print(type(radius))
            radius = int(radius)
            cv2.circle(img, Cir1, radius, orange)   
            cv2.imshow(title, img)
            print("Circle_is_finish")
            Cir1 = -1
            
cv2.imshow(title, img)                                         
cv2.setMouseCallback(title,OnMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()