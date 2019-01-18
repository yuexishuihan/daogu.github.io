import tensorflow as tf
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
# 创建一个变量，并用for循环对变量进行赋值操作

# 创建一个变量num
num = tf.Variable(0,name = "count")

# 创建一个加法操作，把当前的数字+10
new_value = tf.add(num,10)
# 创建一个赋值操作，把new_value赋值给num
op = tf.assign(num,new_value)

with tf.Session() as sess:
    # 初始变量
    sess.run(tf.global_variables_initializer())
    # 打印最初num的值
    print(sess.run(num))
    # 创建一个for循环，每次给num+10,并打印出来
    for i in range(5):
        sess.run(op)
        print(sess.run(num))