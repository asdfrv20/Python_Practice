import cv2
                                                    # 주의, 이미지를 가져올 때 순서는 RGB 가 아닌 BGR이다. 
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)      # 이미지 읽어오기 
# print(img.shape)
cv2.imshow('window_title', img)
cv2.waitKey(0)
cv2.destoryAllWindows()


