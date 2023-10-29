import time
from tensorflow import keras

# 开始时间
start = time.time()

# 加载数据集
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# 将数据进行归一化处理，对标签施加one-hot编码
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float')/255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float')/255
train_labels = keras.utils.to_categorical(train_labels)
test_labels = keras.utils.to_categorical(test_labels)


# 构建LeNet-5网络
model = keras.Sequential([
        keras.layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.AveragePooling2D((2, 2)),
        keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),
        keras.layers.AveragePooling2D((2, 2)),
        keras.layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(84, activation='relu'),
        keras.layers.Dense(10, activation='softmax'),
])

model.compile(optimizer=keras.optimizers.RMSprop(lr=0.001), loss=keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

# 训练网络，用fit函数，epochs表示训练多少个回合，batch_size表示每次训练给多大的数据
model.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=2)
# 在测试集上验证模型
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("\n", "test_loss:", test_loss, "test_accuracy:", test_accuracy)
# 结束时间
end = time.time()
print("\n", "Execution Time:", end - start, "s")
