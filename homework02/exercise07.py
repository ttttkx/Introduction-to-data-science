c=int(input("请输入一个正整数："))
g=c/3
i=0

while(abs(g*g*g-c)>0.00000000001):
    g=(g*2+c/(g*g))/3
    i+=1
    
print("{}的立方根是:{}".format(c,g))