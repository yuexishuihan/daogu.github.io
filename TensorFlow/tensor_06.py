import numpy as np
import pandas as pd 
import tensorflow as tf

# 加载数据集，把对输入和结果进行分开
train = pd.read_csv("train.csv")
images = train.iloc[:,1:].values
labels_flat = train['label'].values.ravel()

# 对输入进行处理
images = images.astype(np.float)

images = np.multiply(images,1.0 / 255.0)
print('输入数据的量：（%g,%g）' % images.shape)

image_size = images.shape[1]
print("输入数据的维度=> {0}".format(image_size))

image_width = image_height = np.ceil(np.sqrt(image_size)).astype(np.uint8)
print('图片的长 =>{0}\n图片的高 =>{1}'.format(image_width,image_height))

x = tf.placeholder('float',shape = [None,image_size])

# 对结果进行处理
labels_count = np.unique(labels_flat).shape[0]
print('结果的种类 =>{0}'.format(labels_count))
y = tf.placeholder('float', shape=[ labels_count])

# 进行One-hot编码
def dense_to_one_hot(labels_dense,num_classes):
    num_labels = labels_dense.shape[0]
    index_offset =np.arange(num_labels)
    labels_one_hot = np.zeros(num_labels)
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot

labels = dense_to_one_hot(labels_flat,labels_count)
labels = labels.astype(np.uint8)

print('结果的数量：({0[0]},{0[1]})'.format(labels.shape))

# 把输入数据划分训练集和验证集
# 把40000个数据作为训练集，2000个数据作为验证集
VALIDATION_SIZE = 2000

validation_images = images[:VALIDATION_SIZE]
validation_lables = labels[:VALIDATION_SIZE]

train_images = images[VALIDATION_SIZE:]
train_labels = labels[VALIDATION_SIZE:]

# 对训练集进行分批
batch_size = 100
n_batch = len(train_images)/batch_size

