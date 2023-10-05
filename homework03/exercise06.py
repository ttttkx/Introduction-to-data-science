print("第6题")

score=int(input("请输入考试成绩："))

if(score<60):
    print("不合格")
elif(60<=score<=74):
    print("合格")
elif(75<=score<=89):
    print("良好")
elif(score>=90):
    print("优秀")