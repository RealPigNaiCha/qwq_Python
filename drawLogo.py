#可参照编程模板，完善代码实现图形绘制，亦可以自行设计编码实现。
import turtle

def Draw():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.end_fill()

for i in range(3):
    Draw()

turtle.hideturtle()
turtle.done()