"""draw random python 
created in 2024/02/29
Author:RealPigNaiCha"""
from turtle import *
import random
pythonLen=random.randint(1,10)
setup(150*pythonLen,600)
colorList=["red","cyan","green","blue","yellow","black","magenta","seashell","gold","pink","purple","tomato"]
penup()
forward(-120*pythonLen/2)
pendown()
pensize(25)
seth(-40)
for i in range(pythonLen):
    pencolor(colorList[random.randint(0,len(colorList)-1)])
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
forward(40)
circle(16,180)
forward(40*2/3)
done()