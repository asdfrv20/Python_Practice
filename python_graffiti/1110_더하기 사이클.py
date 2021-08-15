# while문 
# 백준 - 1110번

import sys
import copy

N = int(sys.stdin.readline())

dummy = copy.copy(N)

# 입력된 수가 10보다 작을 때
if dummy < 10:
    dummy *= 10
    N *= 10 

# 사이클 구하기 
cycle = 0
while True:
    dummy_10 = dummy//10
    dummy_1 = dummy%10
    dummy_add = (dummy_10 + dummy_1)%10
    # print("dummy_10: ", dummy_10)
    # print("dummy_1: ", dummy_1)
    # print("dummy_add: ", dummy_add)

    dummy = dummy_1*10 + dummy_add
    # print(dummy)

    cycle += 1
    if dummy == N:
        break
print(cycle)


