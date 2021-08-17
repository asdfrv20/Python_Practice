import turtle as t 
import random

def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

def turn_up():
    t.setheading(90)
    t.forward(10)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

def turn_down():
    t.setheading(270)
    t.forward(10)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

def turn_left():
    t.setheading(180)
    t.forward(10)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

def turn_right():
    t.setheading(0)
    t.forward(10)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

def clear_bg():
    '''화면 클리어'''
    t.clear()

t.bgcolor("black")
t.title("거북이 도장 찍기")
t.shape('turtle')
t.pensize(10)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.onkeypress(clear_bg, "space")
t.listen()

t.mainloop()
