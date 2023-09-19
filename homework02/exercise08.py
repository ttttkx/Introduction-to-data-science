import math

# 1.割圆法
 
def cutting_circle(n):      # n为分割次数
    side_length = 1  # 初始边长
    edges = 6  # 初始边数

    def length(x):
        h = math.sqrt(1-(x /2)**2)
        return math.sqrt((x /2)**2 + (1-h)**2)
    for i in range(n):
        side_length = length(side_length)
        edges *=2
        pi = side_length*edges/2

    return pi
 
times = 10         # 割圆次数
pi =cutting_circle(times) #调用函数返回值

print(f'割圆法计算的圆周率为：{pi:.10f}')


# 2.无穷级数法
 
def leibniz_of_pi(error):
    a = 1
    b = 1
    sum = 0
    while 1/ b > error:
        if a % 2 != 0:
            sum += 1 / b
        else:
            sum -=  1/ b
        a += 1
        b += 2
    pi = sum*4
    return pi
 
threshold = 0.0000001
print("级数法计算的圆周率为：{:.10f}".format(leibniz_of_pi(threshold))) 
    
# 3.蒙特卡洛法

import random
def monte_carlo_pi(times):
    a = 0
    count = 0
    while a < times:
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <=1:
            count += 1
        a +=1
    return 4*count / a 
 
times = 10000000        # 产生点数量
print("蒙特卡洛法计算的圆周率为：{:.10f}".format(monte_carlo_pi(times)))  

print(f'math库中的圆周率常量值为{math.pi:.10f}')                          