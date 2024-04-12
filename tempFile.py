score=eval(input())
if score >= 60 :
    grade="D"
elif score >= 70 :
    grade="C"
elif score >= 80 :
    grade="B"
elif score >= 90 :
    grade="A"
print("输入成绩属于级别"+grade)