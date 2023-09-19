A=[["狼",1],["羊",1],["菜",1]]  #原岸
B=[["狼",0],["羊",0],["菜",0]]  #对岸
size=len(A)
count=-1
number=-1

def judge(A):    #判断某岸上状态是否合法
    if A[1][1]==1 and A[0][1]+A[2][1]==1:
        return False
    else:
        return True
    
def A_to_B():    #挑选一个物送到对岸，使两岸状态合法
    global number
    global count
    for i in range(size):
        if A[i][1]==1 and i!=number:
            A[i][1]-=1
            if judge(A):
                B[i][1]+=1
                number=i
                print("人和%s过河"%A[i][0])
                count+=1
                break
            else:
                A[i][1]+=1
                continue
        else:
            continue
           
def B_to_A():    #挑选一个不为刚运过来的物送回原岸
    global number
    global count
    if judge(B)==False:
        for j in range(size):
            if B[j][1]==1 and j!=number:
                B[j][1]-=1 
                A[j][1]+=1
                number=j
                print("人和%s返回"%B[j][0])
                count+=1
                break
    else:
        if B[0][1]+B[1][1]+B[2][1]==3:
            print("任务完成")
        else:
            print("人返回")  
            
def sucess():
    if B[0][1]+B[1][1]+B[2][1]==3:
        return True
    else:
        return False   
    
while 1:
    A_to_B()
    B_to_A()
    if sucess():
        break
