# 1.14M = 740*547*3*8 bit/8 (B)
import cv2
img = cv2.imread('hezhao.jpg')
(b,g,r) = img[100,100]
print(b,g,r)
# 图片是以bgr的顺序储存 图片的像素是一个矩阵[w,h]
# 10 100 --- 120 100 
for i in range(1,110):
	img[10+i,100] = (0,0,255)
cv2.imshow('image',img)
cv2.waitKey()






