import tensorflow as tf
# 创建一个变量占位符input1
input1 = tf.placeholder(tf.float32)
# 创建一个变量占位符input2
input2 = tf.placeholder(tf.float32)

# 创建一个加法操作，把input1和input2相乘
new_value = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(new_value,feed_dict = {input1:23.0,input2:11.0}))