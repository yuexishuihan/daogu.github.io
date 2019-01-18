import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf

v1 = tf.constant([(2,3)])

# 创建一个常量v2，他是一个2行1列的矩阵
v2 = tf.constant([[2],[3]])

# 创建一个矩阵乘法
product = tf.matmul(v1,v2)

print(product)

# 定义一个会话
sess = tf.Session()
# 运算乘法，得到结果
result = sess.run(product)
print(result)
sess.close()
