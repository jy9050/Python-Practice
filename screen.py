import turtle
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("yellow")
t.color("blue")
t.pensize(5)
t.begin_fill()
for i in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()
turtle.done()