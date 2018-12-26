# CURD
import numpy as np
data1 = np.array([1,2,3,4,5])
print(data1)
data2 = np.array([[1,2],
				[3,4]])
print(data2)
# 打印维度
print(data1.shape,data2.shape)

# zeros ones
print(np.zeros([2,3]),np.ones([2,2]))

# 改查
data2[1,0] = 5
print(data2)
print(data2[1,1])
print('*'*40)
# 基本运算
## 算术加减乘除
data3 = np.ones([2,3])
print(data3*2)
print(data3+2)
print(data3/2)
print(data3-2)
print('*'*40)
# 矩阵 乘 加
data4 = np.array([[1,2,3],[4,5,6]])
print(data3+data4)
print(data3*data4)
data5 = np.array([[1,2],[3,4],[5,6]])
print(np.dot(data3,data5))

