import turtle as t
import random 

def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

def leftClick(x,y):
    t.hideturtle()
    t.goto(x,y)
    t.setheading(random.randint(0,360))
    t.shapesize(random.randint(1,10))
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.stamp()

def rightClick(x,y):
    t.clear()

t.title("거북이 도장 찍기")
t.shape('turtle')
t.speed(0)
t.penup()

t.onscreenclick(leftClick, 1)
t.onscreenclick(rightClick,3)
t.listen()

t.mainloop()