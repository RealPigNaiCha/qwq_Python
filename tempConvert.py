'''tempConvert.py
Author:RealPigNaiCha
Created in 2024/2/28/11:14'''
tempStr=input("请输入带有符号的温度值：")
if tempStr[-1] in ['F','f']:
    C=(eval(tempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif tempStr[-1] in ["C","c"]:
    F=1.8*eval(tempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误！")