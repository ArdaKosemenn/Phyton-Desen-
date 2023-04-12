import turtle
sc=turtle.Screen()
spiral = turtle.Turtle()
spiral.speed(11)
sc.bgcolor("black")
col=["cyan","gray","white","purple"]
c=0

for i in range(50):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    
    if c==3:
        c=0
    else:
        c+=1