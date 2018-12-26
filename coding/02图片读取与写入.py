import tensorflow as tf
import cv2
img = cv2.imread('hezhao.jpg')
cv2.imwrite('image1.jpg',img)
cv2.imshow('image',img)
cv2.waitKey()
