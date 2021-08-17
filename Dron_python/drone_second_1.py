import turtle 

color = ['red', 'orange', 'yellow', 'green', 'blue']

win = turtle.Screen()
win.bgcolor("black")

t = turtle.Turtle()
t.pencolor("yellow")
t.pensize(1)
t.hideturtle()
t.speed(0)
for i in range(1,600):
    t.pencolor(color[i%5])
    t.forward(i)
    t.right(143)

win.mainloop()