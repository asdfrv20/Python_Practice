# while 문
# 백준 10951번
# ※주의 - while문에서 EOF가 발생하는 경우에 loop가 끝나도록 설정하기 

import sys 

result = []
while True:
    try:
        A, B = map(int, sys.stdin.readline().split(' '))
        result.append(A+B)
    except:
        break
    
i = 0
while True:    
    if i == len(result):
        break
    print(f"{result[i]}")
    i += 1