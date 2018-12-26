import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

date = np.linspace(1,15,15)
beginPrice = np.array([2.3,4.,6.,7.,8.,3.4,6.4,3.5,6.7,8.9,2.6,9.,1.5,7.8,7.4])
endPrince = np.array([2.35,2.76,4,4.6,7.6,3.6,8.9,6.4,7.,4.3,7.3,2.7,2.4,4.7,5.9])
plt.figure()
for i in range(0,15):
	# 柱状图
	dataOne = np.zeros([2])
	dataOne[0] = i
	dataOne[1] = i
	priceOne = np.zeros([2])
	priceOne[0] = beginPrice[i]
	priceOne[1] = endPrince[i]
	if endPrince[i] > beginPrice[i]:
		plt.plot(dataOne,priceOne,'r',lw=8)
	else:
		plt.plot(dataOne,priceOne,'g',lw=8)


# 搭建神经网络
##　输出层
dataNormal = np.zeros([15,1])
priceNormal = np.zeros([15,1])
for i in range(0,15):
	dataNormal[i,0] = i/14.0
	priceNormal[i,0] = i/10
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])
## 隐藏层
w1 = tf.Variable(tf.random_uniform([1,10],0,1))
b1 = tf.Variable(tf.zeros([1,10]))
wb1 = tf.matmul(x,w1) + b1
layer1 = tf.nn.relu(wb1)
## 输出层
w2 = tf.Variable(tf.random_uniform([10,1],0,1))
b2 = tf.Variable(tf.zeros([15,1]))
wb2 = tf.matmul(layer1,w2) + b2
layer2 = tf.nn.relu(wb2)
loss = tf.reduce_mean(tf.square(y-layer2))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())	
	for i in range(0,100):
		sess.run(train_step,feed_dict={x:dataNormal,y:priceNormal})
		pred = sess.run(layer2,feed_dict={x:dataNormal})
		predPrice = np.zeros([15,1])
		for i in range(0,15):
			predPrice[i,0] = (pred*10)[i,0]
		plt.plot(date,predPrice,'b',lw=2)
plt.show()