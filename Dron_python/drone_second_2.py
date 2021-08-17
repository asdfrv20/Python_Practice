import turtle
import random

win = turtle.Screen()
win.bgcolor("black")

t = turtle.Turtle('turtle')
t.speed(0)
t.pencolor('yellow')
t.hideturtle()

t.penup()
t.goto(0,-100)
t.pendown()

for i in range(0, 200, 1):
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r,g,b)
    t.circle(i)

win.mainloop()