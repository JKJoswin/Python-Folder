import turtle

win=turtle.Screen()
t=turtle.Turtle()
win.screensize(700,700)
win.bgcolor("Green")
win.title("Canvas")
t.color("black")
t.shape("turtle")
for i in range(0,4):
    t.forward(90)
    t.left(90)
turtle.done()