print("第7题")

def func(n, m):
    temp = n % m
    while temp != 0:
        n = m
        m = temp
        temp = n % m
    return m

m,n=(input("请输入两个正整数：")).split(" ")
m=int(m)
n=int(n)
print("最大公倍数是：%d"%func(m,n))