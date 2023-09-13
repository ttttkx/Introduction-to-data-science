n=int(input("请输入一个数："))
outcome=1
for i in range(1,n+1):
    outcome*=i
print("{}的阶乘是：{}".format(n,outcome))