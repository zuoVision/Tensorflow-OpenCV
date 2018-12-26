import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,9,4,6,2,15])
# 折线
plt.plot(x,y,'r',lw=10) # lw - 线宽 'g' - 颜色
# 柱状
plt.bar(x,y,0.2,alpha=0.5,color='b') # alpha-透明度
plt.show()


