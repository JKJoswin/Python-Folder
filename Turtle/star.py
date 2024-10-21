import turtle

win=turtle.Screen()
win.screensize(700,700)
t=turtle.Turtle()
win.bgcolor("black")
t.shape("turtle")
t.color("white")

for i in range(0,3):
    t.forward(200)
    t.left(120)
t.left(90)
t.penup()
t.forward(120)
t.right(90)
t.pendown()
for i in range(0,3):
    t.forward(200)
    t.right(120)
turtle.done()