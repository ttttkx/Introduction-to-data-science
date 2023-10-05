"""插入排序大致流程：
    先取数组的第二个数，将其与第一个数比较，如果第二个数更小，就将它插入第一个数的左边，否则不进行任何操作
    同理，接下来取出第三个数，依次与第一，二个数进行比较，并插入到正确的位置
    以此类推，即可完成排序
"""
print("第12题")

def InsertSort(a,n):
    for i in range(1,n):
        index = i-1 
        tmp = a[i] 
        while index >= 0:
            if tmp < a[index]:
                a[index + 1] = a[index] 
                index-=1
            else:
                break
        a[index + 1] = tmp

arr=[3,44,38,5,47,15,36,26,27]
InsertSort(arr, len(arr))
print(arr)