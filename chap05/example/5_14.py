import numpy as np, cv2

data = [ 3, 6, 3, -5, 6, 1, 2,-3, 5]				    # 1차원 리스트 생성
m1 = np.array(data, np.float32).reshape(3,3)
m2 = np.array([2, 10, 28], np.float32)

ret, inv = cv2.invert(m1, cv2.DECOMP_LU)                # 역행렬 계산
if ret:
    dst1 = inv.dot(m2)                                  # numpy 제공 행렬곱 함수
    print("[inv] = \n%s\n" % inv)
    print("[dst1] =", dst1.flatten())                   # 다행 1열 행렬을 한행에 표시
else:
    print("역행렬이 존재하지 않습니다.")


