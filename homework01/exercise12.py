x=float(input("请输入一个数："))
i=0
if(x<0):
    while(1):
        if((i-1)*(i-1)*(i-1)<=x and i*i*i>=x):
            break
        i-=1          #先求出三次方根的大概范围
        
    mid=(i+i-1)/2
    m=i-1
    n=i
    for j in range(0,20):  
        if(mid*mid*mid<=x):
            m=mid
            mid=(mid+n)/2            
        else:
            n=mid
            mid=(m+mid)/2           
    print("{}的三次方根是：{}".format(x,mid))           #用二分法逼近三次方根
    
else:
    while(1):
        if((i+1)*(i+1)*(i+1)>=x and i*i*i<=x):
            break
        i+=1
        
    mid=(i+i+1)/2
    m=i
    n=i+1
    for j in range(0,20):  
        if(mid*mid*mid<=x):
            m=mid
            mid=(mid+n)/2
        else:
            n=mid
            mid=(m+mid)/2           
    print("{}的三次方根是：{}".format(x,mid))  
        
