x,y,z=input("请输入3个数并用逗号分隔:").split(",")
lst1=[]
lst1.append(x)
lst1.append(y)
lst1.append(z)
lst1=sorted(lst1)
print(lst1[0],lst1[1],lst1[2])