print("第1题")

def d2b(x):
    x -= int(x)
    ls1 = []

    while x:
        x *= 2
        ls1.append(1 if x>=1. else 0)
        x -= int(x)

    for i in range(0,len(ls1)):
        print(ls1[i],end="")    

x=float(input("请输入一个十进制的小数："))

print(bin(int(x))[2:],end=".")

d2b(x)