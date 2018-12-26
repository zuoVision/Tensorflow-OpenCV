import cv2
img = cv2.imread('hezhao.jpg',1)

# jpg图片压缩
# 压缩图片质量 参数范围0-100 参数越小压缩比越低
# 有损压缩————牺牲图片质量
cv2.imwrite('imageTest.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,0])

# png压缩
# 1.无损压缩
# 2.透明度属性
# 3.参数范围0-9  参数越小压缩比越高
cv2.imwrite('imageTest.png',img,[cv2.IMWRITE_PNG_COMPRESSION,0])
