import turtle

a=turtle.Turtle()
screen = turtle.Screen()
a.speed(4)
a.width(20)
screen.bgcolor("black")

col=("yellow","brown","pink","orange","red","blue","cyan","maroon","violet","gray","green","beige","silver")
a.penup()
a.back(200)
a.pendown()
a.pencolor("maroon")
a.write("By: @arda_ksmn",align="right",)
a.penup()
a.forward(100)
a.pendown()

for i in range (20):
    a.pencolor(col[i%13])
    a.forward(250)
    a.right(144)
