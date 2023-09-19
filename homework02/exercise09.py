import random 
import math 

N = 10000000 
C = 0 

for i in range(N): 
    x = random.uniform(2.0,3.0) 
    y = random.uniform(0.0,12.3) 
    
    if y <= x**2 + 4*x*math.sin(x): 
        C += 1 
        
I = C / N * 12.3
print("定积分的值为:",end="")
print(format(I,'.4f'))
