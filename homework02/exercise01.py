# 发现拆分的数不会超过3，因为x,y>=2时，x*y>=x+y;
# 为了使乘积尽量大，应该先尽可能拆除3，然后拆除2

# 考虑所有的n除以3的情况：
# 可以被3整除，那么就全部拆为3，如:9=3+3+3;
# 被3除余1，可以拆为形如3+3+……+3+4，即3+3+……+3+2+2，如10=3+3+2+2;
# 被3除余2，可以拆为形如3+3+……+3+2，如11=3+3+3+2

n=int(input("请输入一个正整数："))
num_3=0
num_2=0

if(n<=3):
    print(n)
else:
    if(n%3==0):
        num_3=int(n/3)
        for i in range(0,num_3):
            print(3,end=" ")
    elif(n%3==1):
        num_3=int((n-4)/3)
        num_2=2
        for i in range(0,num_3):
            print(3,end=" ")
        for i in range(0,num_2):
            print(2,end=" ")
    else:
        num_3=int((n-2)/3)
        num_2=1
        for i in range(0,num_3):
            print(3,end=" ")
        for i in range(0,num_2):
            print(2,end=" ")
    