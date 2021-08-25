# 함수 
# 백준 - 1065번 문제 
# 각 자리 정수가 등차수열을 이룬다-> 0역시 포함

import sys
import copy

def checkHanNumber(number):
    # number를 각 자리 정수로 나누기
    dummy = copy.copy(number)
    num_list=[]
    while dummy>=10:
        num_list.append(dummy%10)
        dummy //= 10
    num_list.append(dummy)
    # print(num_list)

    # 한수 검사
    ## 한 자리 수 일 때, 항이 1개 뿐이므로 등차수열이라고 할 수 있음.
    if len(num_list) == 1:
        return True
    ## 두 자리 수 일 때, 항이 2개 이므로 두 항의 차이를 가지는 등차수열이라고 할 수 있음.
    elif len(num_list) == 2:
        return True
    ## 세자리 이상 일 때, 각 항의 차이 "d"를 list로 저장하여. d.count(d[0])==len(d)인지 검사 
    else:
        d = []
        for i in range(len(num_list)-1):
           d.append(num_list[i+1]-num_list[i])
        if d.count(d[0]) == len(d):
            return True

N = int(sys.stdin.readline())

count = 0
for number in range(1, N+1):
    check_result = checkHanNumber(number)
    if check_result == True:
        count += 1
print(count)
