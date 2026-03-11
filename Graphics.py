import turtle
t=turtle.Turtle()
list1=("yellow","red","blue","green","purple")
t.speed(10)
for i in range(200):
    t.color(list1[1%5])
    t.pensize(i/5+1)
    t.forward(i)
    t.left(69)
turtle.done    



