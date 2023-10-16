#-*- coding:utf-8 -*-
import numpy as np

X=np.array([[1,2,3],[1,-1,4],[2,1,3],[1,3,-1]])
c=np.cov(X, rowvar=False)

def Solve(mat, max_itrs, min_delta):
    """
    mat 表示矩阵
    max_itrs 表示最大迭代次数
    min_delta 表示停止迭代阈值
    """
    itrs_num = 0
    delta = float('inf')
    N = np.shape(mat)[0]
    # 所有分量都为1的列向量
    x = np.ones(shape=(N, 1))

    while itrs_num < max_itrs and delta > min_delta:
        itrs_num += 1
        y = np.dot(mat, x)
        m = y.max()
        x = y / m
        
    print("特征值：",y)
    print("特征向量：",x)

IOS=c
Solve(IOS, 10, 1e-10)
