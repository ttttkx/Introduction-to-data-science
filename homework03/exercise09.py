print("第9题")

arr1=[2,5,3,4,7,6,8]
arr2=[]

for i in range(0,len(arr1)):
    arr2.append(1)

for i in range(0,len(arr1)):
    for j in range(0,len(arr1)):
        if(i!=j):
            arr2[i]*=arr1[j]
            
print(arr2)