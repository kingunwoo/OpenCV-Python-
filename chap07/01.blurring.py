import numpy as np, cv2, time

# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1               # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1               # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32")         # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)                       # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]                    # 출력화소 저장
    return dst                                                  # 자료형 변환하여 반환

# 회선 수행 함수 - 화소 직접 근접
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):                    # 마스크 원소 순회
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter , j + v - xcenter
                    sum += image[y, x] * mask[u, v]           # 회선 수식
            dst[i, j] = sum
    return dst

def filter3(image, filter):
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
    
    

image = cv2.imread("/home/gun/Desktop/OpenCV_with_python/OpenCV-Python-/chap07/images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 블러링 마스크 원소 지정     
data = [1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25 ]

mask = np.array(data, np.float32).reshape(5, 5)

start_time = time.time()
blur3 = filter3(image, mask)
end_time = time.time()

filter3_time = end_time - start_time

start_time = time.time()
blur1 = filter(image, mask)
end_time = time.time()

filter1_time = end_time - start_time

start_time = time.time()
blur2 = filter2(image, mask)
end_time = time.time()

filter2_time = end_time - start_time

print(filter1_time)
print(filter2_time)
print(filter3_time)

#cv2.imshow("image", image)
#cv2.imshow("blur", blur1.astype("uint8"))
#cv2.imshow("blur2", blur2.astype("uint8"))cv2.imshow("blur", blur1.astype("uint8"))
#cv2.imshow("blur3", blur3.astype("uint8"))
#cv2.waitKey(0)