# 1차원 배열
# 백준 - 2562번
# python list의 자체 명령어 잘 사용할 것

import sys

numbers = []
while True:
    try:
        number = int(sys.stdin.readline())
        numbers.append(number)
    except:
        break

result = max(numbers)
print(result)
print(numbers.index(result)+1)