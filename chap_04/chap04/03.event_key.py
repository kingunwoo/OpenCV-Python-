import numpy as np
import cv2

## switch case문을 사전(dictionary)으로 구현
switch_case = {
	ord('a'): "a키 입력",               		# ord() 함수- 문자를 아스키코드로 변환
  	ord('b'): "b키 입력",
  0x41: "A키 입력",
  int('0x42', 16): "B키 입력",          		# 16진수인 0x42를 10진수로 변환하면 66임
  2424832: "왼쪽 화살표키 입력",      		    # 0x250000
  2490368: "윗쪽 화살표키 입력",      		    # 0x260000
  2555904: "오른쪽 화살표키 입력",    		    # 0x270000
  2621440: "아래쪽 화살표키 입력"        		# 0x280000
}

img = np.zeros((200,300), np.float16)
img[:] = 200
title1 = 'title1'
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)

while(True):
    key = cv2.waitKeyEx(100)
    
    if(key == 27):
        break
    
    elif(key != -1):
        result = switch_case[key]
        print(result)
    
    else:
        print('-1')
    
cv2.destroyAllWindows()
