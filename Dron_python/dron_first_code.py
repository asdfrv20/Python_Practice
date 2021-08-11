# first print() codeing

# 문자열 출력: print()
'''
print("IDLE에서 파이썬 코드를")
print("작성해서 출력해 보는")
print("예제입니다")
print("포항항 항하항항")   # 문자열 출력
'''

# 문자열 연산
'''
print("안녕하세요" + "오수진입니다")
print("안녕하세요"*10)
'''

# print 속성: sep, end 
'''
print("Hello")
print("Dron Coding")

print("Hello", end='@')
print("Dron Coding")
'''

# Quiz1
'''
## case1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!")
## case2
print("Twinkle, twinkle, little star,","How I wonder what you are!", sep='\n\t')
'''


# 문자열 입력: input()
'''
input("이름을 입력하세요>>> ")
'''

'''
print(input("이름을 입력하세요:"))
'''


# 변수(Variable)
# : 정보를 저장해 두는 공간 - 어떤 값을 저장하는 메모리 공간
'''
num1 = 20
num2 = num1
'''

# 키워드 확인하기
'''
import keyword
print(keyword.kwlist)
'''

# input을 변수에 할당하기
'''
name = input("이름을 입력하세요 : ")
ban = input("반 : ")

print(name)
print(ban)
'''

# Quiz2
'''
name = input("이름을 입력하세요 : ")
print(f"{name} 만나서 반가워!")
print("%s 만나서 반가워!" %name)
print(name, "만나서 반가워!")
'''

# 산술연산자


# 형 변환(Type casting)
# int(x)
# float(x)
# str(x)
# bool(x)


# 문자열의 format(x) 함수
'''
ret = "{} {}".format(10,20)
print(ret)
ret = "{} {} {}".format(10,20,30)
print(ret)
'''

'''
a = "python"
b = 3
c = 3.8
print("{}버전".format(a))
print("{}버전 {}".format(a, b))
print("{}버전 {}과 {}".format(a, b, c))
'''


# 조건문 if
# if 조건표현식1:
#     code
# elif 조건표현식2:
#     code
# else:
#     code
'''
a = 10
if a == 10:
    print("a is 10")
else:
    print("a is not 10")
'''    


# 실습 - 조건문의 기본 사용
# 정수의 양,0,음 구분하는 프로그램
'''
num = int(input("정수입력: "))
if num == 0:
    print("0 입니다.")
elif num > 0:
    print("양수입니다.")
else:
    print("음수입니다.")
'''


# 실습 - 조건문의 기본 사용
# : 짝수와 홀수를 구분할 수 있는 프로그램 
'''
number = int(input("정수 입력>> "))
if number%2 == 0:
    print(f"{number}는 짝수 입니다.")
else :
    print(f"{number}는 홀수 입니다.")
'''    

# 실습 - 성적관리
'''
score = int(input("성적을 입력하세요>>> "))
if score >= 90 :
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
'''

'''
print("\    /\ ")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
'''


# 반복문 - for
'''
for i in range(3):
    print(i)
'''

'''
for i in range(5):
    print("Hello")
    print("Dron Coding")
print("end of for")
'''


# 반복문 - while
'''
while False:
    print("never ending stroy")
'''

'''
aaa = True
i = 0
while aaa :
    print(i)
    i += 1
    if i >= 10:
        break

print("end of for")
'''

'''
i = 0
while i<10:
    print(f"{i}번째 반복입니다.")
    i += 1
'''

# turtle 모듈
# n 각형 그리기 
'''
import turtle

n = 8
for i in range(n):
    turtle.forward(100)
    turtle.right(360/n)
'''
'''
import turtle as t
n = 7
for i in range(n):
    t.forward(100)
    t.right(360/n)
'''

'''         
# setx, sety 
import turtle
import time

t = turtle.Turtle('turtle')

t. clear()

t.setx(100)
time.sleep(1)

t.setx(200)
time.sleep(1)

t.sety(200)
'''

'''
# goto
import turtle
import time

turtle.clear()
time.sleep(1)
turtle.goto(100,100)
'''

'''
import turtle as t

t.clear()
t.goto(100,100)
t.sety(-100)
t.home()
'''

'''
import turtle

win = turtle.Screen()
t = turtle.Turtle('turtle')
for i in range(3):
    t.forward(200)
    t.right(120)
'''
'''
import turtle

t = turtle.Turtle('turtle')
t.color('red')
t.pensize(5)
for i in range(3):
    t.forward(200)
    t.right(120)
'''

'''
import turtle as t
import time

t.shape('turtle')
t.color('yellow')
t.pensize(5)
t.speed(0)

t.color("red")
t.forward(80)
t.stamp()
s1 = t.stamp()

t.color("green")
t.forward(80)
time.sleep(1)
t.stamp()
s2 = t.stamp()

t.color("yellow")
t.forward(80)
t.stamp()
s3 = t.stamp()

time.sleep(1)
t.clearstamp(s1)
'''

'''
import turtle as t
import time

t.shape('turtle')
t.color('blue')
t.pensize(5)
t.speed(5)

# t.dot(100)
t.fillcolor('purple')
t.begin_fill()
t.circle(-100, 360, 15)
t.end_fill()
'''

'''
import turtle
import random

t = turtle.Turtle('turtle')
t.pensize(5)

color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

n = 6
for i in range(n):
    t.pencolor(color[random.randint(0,6)])
    t.forward(200)
    t.right(360/n)
'''

'''
import turtle

t = turtle.Turtle('turtle')
t.pensize(5)
t.speed(0)

color = ['red', 'orange', 'yellow', 'green']

for i in range(60):
    for j in range(4):
        t.pencolor(color[j])
        t.forward(200)
        t.right(360/4)
    t.right(360/60)
'''

import turtle

win = turtle.Screen()
win.bgcolor('black')

t = turtle.Turtle('turtle')
t.speed(0)
t.pencolor('yellow')

for j in range(600):
    t.forward(j)
    t.right(71)
    
    



# Lotto 번호 출력 code
'''
import random

lotto_num = []
while True:
    # 임시 random 숫자 생성하기 
    temp_num = random.randint(1,45)
    
    # lotto_num에 포함된 숫자인지 검사 
    count = 0
    for num in lotto_num:
        if num != temp_num:
            count += 1
    if count == len(lotto_num):
        lotto_num.append(temp_num)

    # 결과 출력
    if len(lotto_num) == 7:
        print("Lotto Number: ", end='')
        for num in lotto_num[:-1]:    
            print(num, end=' ')
        print(f"\nBonus Number: {lotto_num[6]}")
        break    
'''


