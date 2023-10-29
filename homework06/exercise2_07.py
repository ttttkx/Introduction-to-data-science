from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense,Conv2D,MaxPool2D

LeNet5 = Sequential([
    Conv2D(filters=6, kernel_size=5, strides=1, activation='sigmoid',input_shape=(32,32,1)),
    MaxPool2D(pool_size=2, strides=2),
    Conv2D(filters=16, kernel_size=5, strides=1, activation='sigmoid'),
    MaxPool2D(pool_size=2, strides=2),
    Conv2D(filters=120, kernel_size=5, strides=1, activation='sigmoid'),
    Flatten(),
    Dense(units=84, activation='sigmoid'),
    Dense(units=10, activation='softmax')
])

LeNet5.summary()
