import tensorflow as tf
print('情况1：当没有设置图级seed和操作级seed时，生成的随机数是随机的 ')
a = tf.random_uniform([1])
b = tf.random_normal([1])
print("Session 1")
with tf.Session() as sess1:
    print(sess1.run(a))  # generates 'A1'
    print(sess1.run(a))  # generates 'A2'
    print(sess1.run(b))  # generates 'B1'
    print(sess1.run(b))  # generates 'B2'
print("Session 2")
with tf.Session() as sess2:
    print(sess2.run(a))  # generates 'A3'
    print(sess2.run(a))  # generates 'A4'
    print(sess2.run(b))  # generates 'B3'
    print(sess2.run(b))  # generates 'B4'

print('情况2：当设置操作级seed时，生成的随机数是同一组随机数，没有设置操作级seed的操作，生成的随机数是随机的 ')
a = tf.random_uniform([1], seed=1)
b = tf.random_normal([1])
# Repeatedly running this block with the same graph will generate the same
# sequence of values for 'a', but different sequences of values for 'b'.
print("Session 1")
with tf.Session() as sess1:
    print(sess1.run(a))  # generates 'A1'
    print(sess1.run(a))  # generates 'A2'
    print(sess1.run(b))  # generates 'B1'
    print(sess1.run(b))  # generates 'B2'
print("Session 2")
with tf.Session() as sess2:
    print(sess2.run(a))  # generates 'A1'
    print(sess2.run(a))  # generates 'A2'
    print(sess2.run(b))  # generates 'B3'
    print(sess2.run(b))  # generates 'B4'
print('情况3：当设置图级seed, 将会生成同一组随机数，如果设置操作级seed又和情况2相同')
tf.set_random_seed(1234)
a = tf.random_uniform([1])
b = tf.random_normal([1])
# Repeatedly running this block with the same graph will generate the same
# sequences of 'a' and 'b'.
print("Session 1")
with tf.Session() as sess1:
    print(sess1.run(a))  # generates 'A1'
    print(sess1.run(a))  # generates 'A2'
    print(sess1.run(b))  # generates 'B1'
    print(sess1.run(b))  # generates 'B2'
print("Session 2")
with tf.Session() as sess2:
    print(sess2.run(a))  # generates 'A1'
    print(sess2.run(a))  # generates 'A2'
    print(sess2.run(b))  # generates 'B1'
    print(sess2.run(b))  # generates 'B2'
