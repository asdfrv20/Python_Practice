# 함수 ~ list 까지 

### lambda식 활용
## lambda(무명 함수): 이름은 없고 몸체만 있는 함수
## 활용: lambda 인수1, 인수2, ... : 수식
'''
sum = lambda x, y: x+y
print("정수의 합: ", sum(1, 2))
print("정수의 합: ", sum(100, 251))
'''

'''
L = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for f in L:
    print(f(3), end=' ')
'''

### 모듈 불러오기
'''
from fibo import *

fib(1000)
'''

### list
'''
## 값으로 호출하기
def func1(x):
    print("x=", x, "id=", id(x))
    x = 42
    print("x=", x, "id=", id(x))

y = 10

print("y=", y, "id=", id(y))
func1(y)
print("y=", y, "id=", id(y))
'''
'''
## 참조로 호출하기: list 활용
def func2(list):
    list[0] = 99

values = [0,1,2,3,4,5,8]
print(values, 'id=', id(values))
func2(values)
print(values, 'id=', id(values))
'''
'''
## 리스트 함축(list comprehensions)
S = [x**2 for x in range(10)]
print(S)

list1 = [3,4,5]
list2 = [x**2 for x in list1]
print(list1)
print(list2)
'''
'''
## 조건이 붙는 list 함축
from math import *

M = [sqrt(x) for x in range(20) if x % 2 ==0]
print(M)
'''
'''
## 문자열을 원소로 갖는 list comprehensions: 단어의 첫 글자만 따오기
list1 = ["Life", "is", "too", "short", "You", "Need", "Python"]
list2 = [word[0] for word in list1]
print(list2)
'''
'''
## 하나의 문장으로 된 문자열을 split으로 나누고 각 단어의 길이를 list로 생성하여 출력하기
str1 = 'Doncount your chickens before they are hatched'
list1 = str1.split()
print('list1=', list1)
print(type(list1))
list2 = [len(word) for word in list1]
print('word_length=', list2)
'''
'''
## 문제풀이(269p): 1~30까지 숫자들 중 피타고라스 정리를 만족하는 숫자들 찾기. 단, list comprehensions를 활용할 것
list1 = [(x,y,z) for x in range(1, 31) for y in range(x,31)
         for z in range(y,31) if x**2+y**2==z**2]
print(list1)
'''

### TIC-TAC-TOE 게임 만들기
'''
from random import randint

def print_board(list):
    print(list[0][0], ' |', list[0][1], '| ', list[0][2] )
    print('---|---|---')
    print(list[1][0], ' |', list[1][1], '| ', list[1][2])
    print('---|---|---')
    print(list[2][0], ' |', list[2][1], '| ', list[2][2])

# game start
print('[TIC-TAC-TOE GAME]')
print('you:O, com:X')
board_list = [[' ' for i in range(3)] for j in range(3)]
win = ' '

while 1:
    # print current status
    print_board(board_list)

    # your input
    while 1:
        you_x = int(input('다음 수의 x좌표를 입력하세요: '))
        you_y = int(input('다음 수의 y좌표를 입력하세요: '))
        if board_list[you_x][you_y] == ' ':
            board_list[you_x][you_y] = 'O'
            break;
        else:
            print('이미 채워진 칸입니다. 다시 입력해주세요 ')

    # com's input
    while 1:
        com_x = randint(0, 2)
        com_y = randint(0, 2)
        if board_list[com_x][com_y] == ' ':
            board_list[com_x][com_y] = 'X'
            break

    # winner judgement
    ## row
    for i in range(3):
        if (board_list[i][1] == board_list[i][0]) and (board_list[i][1] == board_list[i][2]):
            win = board_list[i][1]
            break;
    ## column
    for j in range(3):
        if (board_list[1][j] == board_list[0][j]) and (board_list[1][j] == board_list[2][j]):
            win = board_list[1][j]
    ## diagonal
    if ((board_list[1][1] == board_list[0][0]) and (board_list[1][1] == board_list[2][2])) \
            or ((board_list[1][1] == board_list[0][2]) and (board_list[1][1] == board_list[2][0])):
        win = board_list[1][1]

    # break;
    if win == 'O':
        print("You win!")
        break
    elif win == 'X':
        print("Com win!")
        break
'''

'''
### TIC-TAC-TOE GAME 예제 답안: 승리 판단 부분이 없고, com의 놓는 위치는 비어있는 순서대로 넣는다  
board = [[' ' for x in range(3)] for y in range(3)]
while True:
    # 게임 보드 그리기
    for r in range(3):
        print('  ' + board[r][0] + '|  ' + board[r][1] + '|  ' + board[r][2])
        if (r != 2):
            print('---|---|---')

    # 사용자로부터 좌표를 입력받기
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

    # 사용자가 입력한 좌표를 검사
    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'

    # 컴퓨터가 놓을 위치를 결정. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
'''

### list comprehensive에서 for문이 여려 개 있을 때 어떠한 순서로 적용되는가?
## 결과: 다중 for문처럼 가장 뒤(아래)있는 것들 이 먼저 연산이 된다. 여기에서는 z->y->x 순서
'''
dummy = [(x,y,z) for x in range(100,105) for y in range(10,15) for z in range(1,5)]
print(dummy)
'''

### 지뢰찾기 판 만들기
'''
import random

# 빈 지뢰찾기 판 만들기
board = [[' ' for i in range(10)] for j in range(10)]

# random 함수로 30% 이하의 지뢰 설정
for i in range(10):
    for j in range(10):
        if random.random() < 0.3:
            board[i][j] = 1

# 문자로 지뢰찾기 판 출력 (#:빈공간 // .:지뢰)
for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            print('# ', end=' ')
        else:
            print('. ', end=' ')
    print()
'''

