print("第8题")

import random
import time

#总体来说，选择排序的运行时间比归并排序要短，而且随着数列长度的增长，这个时间差会更加明显

ls1=[]
for i in range(100):
    a = random.randint(1, 1000)
    ls1.append(a)

print("未排序的原数列：")
print(ls1)
    
start =time.time()

#归并排序
def merge(a,tmp,min,mid,max):
    i = min
    j = min
    m = mid + 1
    while j<=mid and m<=max:
        if a[j] <= a[m]:
            tmp[i] = a[j]
            j+=1
        else:
            tmp[i] = a[m]
            m+=1
        i+=1
    if j > mid:
        for k in range(m,max+1):
            tmp[i] = a[k]
            i+=1
    else:
        for k in range(j,mid+1):
            tmp[i] = a[k]
            i+=1
    for k in range(min,max+1):
        a[k] = tmp[k]

def sortMerge(a,tmp,min,max):
    if min < max:
        mid = int((min + max) /2)
        sortMerge(a,tmp,min, mid)
        sortMerge(a,tmp, mid + 1, max)
        merge(a,tmp, min, mid, max)

size =len(ls1)
temp=ls1.copy()
sortMerge(ls1,temp, 0, size - 1)
print("归并排序的排序结果：")
print(ls1)

end = time.time()
print('归并排序运行时间: %s Seconds'%(end-start))

start =time.time()

#选择排序
def selection(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        if min>i:
            tmp=a[i]
            a[i]=a[min]
            a[min]=tmp

selection(ls1,9)
print("")
print("选择排序的排序结果：")
print(ls1)

end = time.time()
print('选择排序运行时间: %s Seconds'%(end-start))

