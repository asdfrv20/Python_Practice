# 브루투 포스
# BEACJOON 1436번 문제 
# ※ 어려움 주의!!

# 내 첫번째 답안 (시간초과)
# 666에서부터 1씩 증가시켜 666이 연속되는 값 찾기 
'''
import copy
import time

N = int(input(""))

# start = time.time()

count = 0
number = 666
while True:
    num_list = []
    # number의 각 자리수를 나누어 num_list에 저장
    dummy_number = copy.copy(number)
    while dummy_number!=0: 
        temp = dummy_number%10
        dummy_number = dummy_number//10
        num_list.append(temp)
    # print("number: ", number)
    # print("dummy_number:", dummy_number)
    # print("num_list: ", num_list)
    # print("")

    # 연속한 666이 있는지 확인(cnt_seq6)
    seq6 = False
    for i in range(len(num_list)-2):
        if num_list[i] == num_list[i+1] == num_list[i+2] == 6:
            seq6 = True
            count += 1
            break
    
    # seq6가 True이면 count 증가
    if seq6:
        print("number: ", number)
        print("count: ", count)
        print("")
        
    
    # count == N 일때, while문 break
    # count != N 일때, number에 1더하고 while문 반복
    if count == N:
        break   
    number += 1

print(number)
# print("time: ", time.time()-start)
'''

# 두번째 답안(답안 틀림)
# 숫자를 1부터 순서대로 발생 시킨 뒤, 666을 그 사이사이에 끼워넣기 
# number 순차 발생 -> list로 각자리 분할 -> 666 끼워넣기 
'''
import time

N = int(input(""))

start = time.time()
# step1: 후보군 발생시키기 
# 0~3000까지의 숫자를 발생시키고 각 자릿수 사이에 666을 넣어준다. 
# 그리고 set으로 정리  
list_666 = []
for temp in range(0,3000): 
    # temp가 1의 자리 숫자일 때, 
    if temp//10 == 0:
        # temp의 1의 자리 아래에 666을 삽입
        dummy_number = temp*(1000) + 666    
        list_666.append(dummy_number)
        # temp의 10의 자리에 666을 삽입
        dummy_number = 666*10 + temp        
        list_666.append(dummy_number)

    # temp가 10의 자리 숫자일 때, 
    elif 0 < temp//10 < 10:
        # temp의 1의 자리 아래에 666을 삽입
        dummy_number = temp*(1000) + 666    
        list_666.append(dummy_number)
        # temp의 1의 자리~10의 자리 사이에 666을 삽입
        dummy_number = ((temp//10)*(10000)) + 666*10 + (temp%10)
        list_666.append(dummy_number)
        # temp의 10의 자리 위에 666을 삽입
        dummy_number = 666*(100) + temp        
        list_666.append(dummy_number) 

    # temp가 100의 자리 숫자일 때
    elif 0 < temp//100 < 10:
        # temp의 1의 자리 아래에 666을 삽입
        dummy_number = temp*(1000) + 666    
        list_666.append(dummy_number)
        # temp의 1의 자리~10의 자리 사이에 666을 삽입
        dummy_number = ((temp//10)*(10000)) + 666*10 + (temp%10)
        list_666.append(dummy_number)
        # temp의 10의 자리~ 100의 자리 사이에 666을 삽입
        dummy_number = (temp//100)*(100000) + 666*(10**2) + (temp%100)
        list_666.append(dummy_number)
        # temp의 100의 자리 위에 666을 삽입
        dummy_number = 666*(1000) + temp        
        list_666.append(dummy_number) 

    # temp가 1000의 자리 숫자일 때
    elif 0 < temp//1000 < 10:
        # temp의 1의 자리 아래에 666을 삽입
        dummy_number = temp*(1000) + 666    
        list_666.append(dummy_number)
        # temp의 1의 자리~10의 자리 사이에 666을 삽입
        dummy_number = (temp//10)*(10000) + 666*10 + (temp%10)
        list_666.append(dummy_number)
        # temp의 10의 자리~100의 자리 사이에 666을 삽입
        dummy_number = (temp//100)*(100000) + 666*(100) + (temp%100)
        list_666.append(dummy_number)
        # temp의 100의 자리~1000의 자리 사이에 666을 삽입
        dummy_number = (temp//1000)*(1000000) + 666*(10**3) + (temp%1000)
        list_666.append(dummy_number)

    list_666 = set(list_666)
    list_666 = list(list_666)

    # list_666의 원소 갯수가 N 이상일 때 종료
    if len(list_666) >= N:
        # print("set list_666 길이:", len(list_666))
        break

list_666.sort()
# print("")
# print("list_666 길이(최종): ", len(list_666))

print(list_666[N-1])

# print("time: ", time.time()-start)
'''

# 세 번째 답안(idea)
# front 666 back 으로 설정한 후,
# 1. front_up(front+1 666 back)과 back_up(front 666 back+1)을 비교
# 2. 더 작은 숫자를 list에 저장 후, 해당 경우의 front 또는 back을 1 증가
#    (예를 들자면, front+1 666 back이 채택 되었다면, 다음으로는 front+2 666 back과 front 666 back+1을 비교)
#     두 수가 같은 경우에는 front_up 채택
# ※ 만드는 핵심 포인트: "문자열 더하기" & "str<->int 형변환 사용하여 크기 비교"
'''
import sys 

N = int(sys.stdin.readline())

front = 0
back = 0

number_666 = []
for i in range(N): 
    # front_up(front+1"666"back) vs back_up(front"666"back+1) 생성(문자열 더하기) & 비교
    # front = 0
    front_up = str(front) + '666' + str(back)



    # 다음 비교할 숫자 채택

'''


# 다섯번째 풀이
# back이 0이면 아래에 붙을 수 없다. 
# front는 0부터 시작하여 일의 자리부터 6의 개수에 따라 앞으로 땡겨지고, 땡겨진 6의 갯수 만큼, back이 그 자리를 0에부터 최대 큰 수로까지 채운다 
# 2자리가 당겨졌다면 back은 00~99이다. 

# 필요한 과정: 문자열로 만들기-> 자릿수 세기-> front의 일의자리부터 연속된 6의 갯수 세기( -> back의 자리수 = (자리수)-(front연속 6의 개수)
'''
import sys 

N = int(sys.stdin.readline())

front = 0
back = 0

count = 0
while True:
    number_666 = str(front)+'666'
    print('number_666:', number_666)
    print('길이:', len(number_666))
    print('666 index:', number_666.index('666'))
    

    # number_666의 길이 & '666'의 index로 back의 자릿수 구하기
    back_position = len(number_666)-(number_666.index('666')+3)
    print('back_position:', back_position)

    # front의 일의 자리 숫자 가까이 연속된 6이 있을 경우
    if back_position != 0:
        dummy = int(number_666[:-(back_position)])*(10**back_position)
        for back in range(10**back_position):
            print(dummy)
            dummy += 1
            count += 1
            print('count:', count)
            # count == N 검사
            if count == N:
                sys.exit()
            print("")
    # front의 일의 자리 숫자 가까이 연속된 6이 없는 경우
    else:
        print(int(number_666))
        count += 1
        print('count:', count)
        # count == N 검사
        if count == N:
            sys.exit()
        print("")

    if count == N:
        break
    front += 1
'''


# 여섯번쨰 풀이: 다섯번째 풀이의 오류 수정 
'''
import sys 
import time

N = int(sys.stdin.readline())

start = time.time()
front = 0
count = 1
while True:
    number_666 = str(front)+'666'   

    # number_666의 길이 & '666'의 index로 back의 자릿수 구하기
    back_position = len(number_666)-(number_666.index('666')+3)

    # front의 일의 자리 숫자 가까이 연속된 6이 있을 경우
    if back_position != 0:
        dummy = int(number_666[:-(back_position)])*(10**back_position)
        for back in range(10**back_position):
            # count == N 검사
            if count == N:
                print(dummy)
                print('time: ', time.time()-start)
                sys.exit()
            # print('number:', dummy)
            # print('count:', count)
            # print("")
            dummy += 1
            count += 1
    # front의 일의 자리 숫자 가까이 연속된 6이 없는 경우
    else:
        # count == N 검사
        if count == N:
            print(int(number_666))
            print('time: ', time.time()-start)
            sys.exit()
        # print('number:', int(number_666))
        # print('count:', count)
        # print("")
        count += 1
        
    front += 1
'''


# 제출 답안 
import sys 



N = int(sys.stdin.readline())

front = 0
count = 1
while True:
    number_666 = str(front)+'666'   

    # number_666의 길이 & '666'의 index로 back의 자릿수 구하기
    back_position = len(number_666)-(number_666.index('666')+3)

    # front의 일의 자리 숫자 가까이 연속된 6이 있을 경우
    if back_position != 0:
        dummy = int(number_666[:-(back_position)])*(10**back_position)
        for back in range(10**back_position):
            # count == N 검사
            if count == N:
                print(dummy)
                sys.exit()
            dummy += 1
            count += 1
    # front의 일의 자리 숫자 가까이 연속된 6이 없는 경우
    else:
        # count == N 검사
        if count == N:
            print(int(number_666))
            sys.exit()
        count += 1
        
    front += 1



# 본영이의 ㄹㅇ 간단 코드(깔끔 주의)
'''
N = int(input())
num = 665
while N:
    num += 1
    if '666' in str(num) : N -= 1
print(num)
'''