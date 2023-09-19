c=2
g=c        #不影响结果
i=0

while(abs(g*g-c)>0.00000000001):
    g=(g+c/g)/2
    i+=1
    
print("将c/2改为c计算的2的平方根是:{}".format(g))


c=2
g=c/4       #影响结果
i=0

while(abs(g*g-c)>0.00000000001):
    g=(g+c/g)/2
    i+=1
    
print("将c/2改为c/4计算的2的平方根是:{}".format(g))