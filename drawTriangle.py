import turtle
turtle.pensize(2)    # 设置画笔宽度为2像素
turtle.color('red')
turtle.forward(160)    # 向小海龟当前行进方向前进160像素
turtle.seth(120)
turtle.fd(160)
turtle.seth(-120)
turtle.fd(160)
turtle.penup()
turtle.seth(0)
turtle.fd(80)
turtle.pendown()
turtle.seth(60)
turtle.fd(80)
turtle.seth(180)
turtle.fd(80)
turtle.seth(-60)
turtle.fd(80)
turtle.hideturtle()
turtle.done()