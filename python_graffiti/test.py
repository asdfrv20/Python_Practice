def show(x,y):      # show함수: 랜덤 위치로 거북이를 이동시키는 함수
    global count
    count = count + 1
    t.hideturtle()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x,y)
    t.showturtle()

import random
import turtle
win = turtle.Screen()
win.setup(700, 700)
t = turtle.Turtle('turtle')
t.penup()
t.onclick(show)     # 이벤트 함수 onclick: 객체를 클릭했을 때, 지정한 event 함수 실행

def checkMinute():
    global time
    time += 1
    timer.clear()

    # 현재 타이머 시간 표시
    timer.write('경과시간: ' + str(time) + '초' + ', 잡은 개수:' + str(count))

    # 1초 후, countMiunute함수 호출하는 쓰레드 생성
    thread = threading.Timer(1, checkMinute())
    if time < 60:  # 1분이 지나면 타이머 및 카운팅 중지
        thread.start()

timer = turtle.Turtle()
timer.penup()
timer.goto(100, 200)
import threading
time = 0
count = 0

# 1분 시간 체크 쓰레드 생성
thread = threading.Thread(target=checkMinute())
thread.start()


win.mainloop()