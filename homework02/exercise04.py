n=2
for i in range(0,n):
    if(i*i<n and (i+1)*(i+1)>n):
        g=i

while(1):
    if(abs(g*g-n)<0.0001):
        ans=g
        break
    else:
        g+=0.00001
        
print("一般方法计算的2的平方根是:{}".format(ans))