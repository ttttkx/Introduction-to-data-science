#-*-coding:utf-8-*-
import numpy as np
import math
import matplotlib.pyplot as plt
 
 
def gd(x, mu=0, sigma=1):
  #由自变量x计算因变量的值
  left = 1 / (np.sqrt(2 * math.pi) * np.sqrt(sigma))
  right = np.exp(-(x - mu)**2 / (2 * sigma))
  return left * right
 
 
if __name__ == '__main__':
  # 自变量
  x = np.random.randn(100)

  # 因变量
  y = gd(x, 0, 1.0)
  
  plt.scatter(x,y)

  plt.show()
