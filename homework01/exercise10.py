str1=input("请输入一个字符串：")
i=1
sign=0
while(i<len(str1)):
    if(str1[i-1]==str1[i]):
        print("该字符串包含连续的相同字符")
        sign=1
        break
    else:
        i+=1
        
if(sign==0):
    print("该字符串不包含连续的相同字符")
        