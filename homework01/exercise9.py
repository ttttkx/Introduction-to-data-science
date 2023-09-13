ls1=input("请输入任意个数的数并用逗号分隔：").split(",")
ls1=[int(i) for i in ls1]
for i in range(0,len(ls1)):
   print(ls1[len(ls1)-i-1],end=" ")
   
i=0
while(i<len(ls1)):
    print(ls1[len(ls1)-i-1],end=" ")
    i+=1
    