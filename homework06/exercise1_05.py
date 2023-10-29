import numpy as np
import time

#①sigmoid函数转换
def sigmoid(z):
    return 1/(1 + np.exp(-z))

#②输入X和θ得到预测值
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))

#③计算损失函数
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1-y, np.log(1 - model(X, theta)))
    return np.sum(left - right)/len(X)

#④计算梯度
def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad

#⑤设定停止策略
STOP_ITER = 0 #迭代次数为停止策略
STOP_COST = 1 #损失函数为停止策略
STOP_GRAD = 2 #梯度为停止策略
def stopCriterion(type, value, threshold):
    if type == STOP_ITER:
        return value > threshold
    elif type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold

#⑥对数据进行洗牌
def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols-1]
    y = data[:, cols-1:]
    return X,y
   
#使用以上模块定义梯度下降求解的函数
def descent(data, theta, batchSize, stopType, thresh, alpha):
    #梯度下降求解
    #batchSize参数指定了使用批量、随机还是小批量梯度下降
    #alpha是学习率
    
    init_time = time.time()
    i = 0 #迭代次数
    k = 0 #batch
    X, y = shuffleData(data)
    grad = np.zeros(theta.shape) #计算梯度
    costs = [cost(X, y, theta)] #损失值
    
    while True:
        grad = gradient(X[k:k+batchSize], y[k:k+batchSize], theta)
        k += batchSize #去batch数量个数倍
        if k >= n:
            k = 0
            X,y = shuffleData(data) #重新洗牌
        theta = theta - alpha * grad #参数更新
        costs.append(cost(X, y, theta))
        i += 1
        
        if stopType == STOP_ITER:
            value = i
        elif stopType == STOP_COST:
            value = costs
        elif stopType == STOP_GRAD:
            value = grad
        if stopCriterion(stopType, value, thresh):
            break
    return theta, i-1, costs, grad, time.time() - init_time

