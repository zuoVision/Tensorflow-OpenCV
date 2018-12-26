import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

data1 = tf.constant(6)
data2 = tf.Variable(2)

# 加 乘 减 除
dataAdd = tf.add(data1,data2)
dataCopy = tf.assign(data2,dataAdd) # dataAdd -> data2
dataMul = tf.multiply(data1,data2)
dataSub = tf.subtract(data1,data2)
dataDiv = tf.divide(data1,data2)

# 占位符 placeholder
a = tf.placeholder(tf.float32,name='a')
b = tf.placeholder(tf.float32,name='b')
data_add = tf.add(a,b)

# 矩阵操作

c = tf.constant([[6,6]])
d = tf.constant([[2],
				[2]])
e = tf.constant([[1,2],
				[3,4],
				[5,6]])
f = tf.constant([[3,3]])

# 矩阵加法、乘法
matMul = tf.matmul(c,d)
matMul_2 = tf.multiply(c,d)
matAdd = tf.add(c,f)

# 特殊矩阵
mat0 = tf.zeros([2,3])
mat1 = tf.ones([2,3])
mat2 = tf.fill([2,3],15) #填充矩阵
mat3 = tf.zeros_like(matMul_2) # 维度像矩阵matMul_2的零矩阵
mat4 = tf.linspace(0.0,2.0,10) # 将0-2均分成10等分
mat5 = tf.random_uniform([2,3],-1,2) # 维度2×3 范围从-1 - 2

# 初始化
init = tf.global_variables_initializer()

# 创建Session
with tf.Session() as sess:
	sess.run(init)
	print(sess.run(dataAdd))
	print(sess.run(dataMul))
	print(sess.run(dataSub))
	print(sess.run(dataDiv))
	print('*'*30)

	print('sess.run(dataCopy):',sess.run(dataCopy))
	print('dataCopy.eval():',dataCopy.eval())  # 相当于默认的sess
	print('tf.get_dafault_session():',tf.get_default_session().run(dataCopy))
	print('*'*30)

	print(sess.run(data_add,feed_dict={a:3,b:4}))
	print('*'*30)

	print(sess.run(e)) #打印整体
	print(sess.run(e[0])) #打印第一行
	print(sess.run(e[1])) #打印第二行
	print(sess.run(e[2])) #打印第三行
	print(sess.run(e[:,0]))	#打印第一列
	print(sess.run(e[:,1]))	#打印第二列
	print(sess.run(e[0,1]))#打印第一行第二列
	print('*'*30)

	print(sess.run(matAdd))
	print(sess.run(matMul))
	print(sess.run(matMul_2))
	print('*'*30)

	print(sess.run(mat0))
	print(sess.run(mat1))
	print(sess.run(mat2))
	print(sess.run(mat3))
	print(sess.run(mat4))
	print(sess.run(mat5))
	print('*'*30)
