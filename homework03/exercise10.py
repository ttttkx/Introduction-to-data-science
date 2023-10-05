print("第10题")

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

number=int(input("请输入一个正整数:"))
if(isprime(number)==True):
    print("是质数")
else:
    print("不是质数")

        