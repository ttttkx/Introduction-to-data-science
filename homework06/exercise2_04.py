import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from pandas import DataFrame
import tensorflow as tf
import numpy as np

x_data=datasets.load_iris().data
y_data=datasets.load_iris().target

np.random.seed(116)
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(116)

x_train=x_data[:-30]
y_train=y_data[:-30]
x_test=x_data[-30:]
y_test=y_data[-30:]
#转换x的数据类型，否则矩阵乘时会报错

x_train=tf.cast(x_train,tf.float32)
x_test=tf.cast(x_test,tf.float32)

train_db=tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)
test_db=tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)

w1=tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1,seed=1))
b1=tf.Variable(tf.random.truncated_normal([3],stddev=0.1,seed=1))
lr=0.1#学习率
train_loss_results=[]#记录每轮loss值，为后续话loss图形提供数据
test_acc=[]#记录每轮acc值，为后续话acc图形提供数据
epoch=500#循环500轮
loss_all=0

#训练神经网络
for epoch in range(epoch):
    for step,(x_train,y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            y=tf.matmul(x_train,w1)+b1
            y=tf.nn.softmax(y)
            y_=tf.one_hot(y_train,depth=3)
            loss = tf.reduce_mean(tf.square(y_-y))
            loss_all +=loss.numpy()

        grads=tape.gradient(loss,[w1,b1])

        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])

    print("Epoch{}, Loss{}".format(epoch,loss_all/4))
    train_loss_results.append(loss_all/4)
    loss_all=0

    total_correct,total_number=0,0
    for x_test,y_test in test_db:
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred=tf.argmax(y,axis=1)
        pred=tf.cast(pred,dtype=tf.int32)
        correct=tf.cast(tf.equal(pred,y_test),dtype=tf.int32)
        correct=tf.reduce_sum(correct)
        total_correct +=int(correct)
        total_number +=x_test.shape[0]
        acc=total_correct/total_number
        test_acc.append(acc)
        print("Test_acc",acc)

plt.title("Loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.plot(train_loss_results,label="$loss$")
plt.legend()
plt.show()
