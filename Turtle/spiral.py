import turtle

win=turtle.Screen()
win.screensize(700,700)
t=turtle.Turtle()
win.bgcolor("black")
t.shape("turtle")
colors=["darkblue","blue","teal","green","darkgreen","seagreen"]
turtle.speed(1000000)
t.hideturtle()

while True:
    for i in range(200):
        t.pencolor(colors[i%len(colors)])
        t.width(i/100+1)
        t.forward(i)
        t.right(59)
    t.left(239)
    for i in range(200,0,-1):
        t.pencolor(colors[i%len(colors)])
        t.width(i/100+1)
        t.forward(i)
        t.left(59)
turtle.done()