import tensorflow as tf

A = [[1, 3, 4, 5, 6]]
B = [[1, 3, 4, 3, 2]]
C = [1.8, 2.2]

with tf.Session() as sess:
    a = sess.run(tf.equal(A, B))
    print(a)

    #cast的作用是“将张量转换成新类型”
    #这里cast将boolean类型转换成float类型（True转换成1，False转换成0）
    b = sess.run(tf.cast(a, dtype=tf.float32))
    print(b)

    #reduce_mean用来求平均值
    c = sess.run(tf.reduce_mean(b))
    print(c)

    #这里cast将float型转换成int型
    d = sess.run(tf.cast(C,dtype=tf.int32))
    print(d)
