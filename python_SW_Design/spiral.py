import turtle
win = turtle.Screen()
t = turtle.Turtle('turtle')
t.speed(300)

color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(360):
    t.pencolor(color[x%6])
    t.pensize(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()
 