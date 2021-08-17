# 브루트 포스
# 백준 - 2798 블랙잭 리뉴얼
import sys

# step1. 첫째 줄 입력 
N, M = map(int, sys.stdin.readline().split())
# step2. 둘째 줄 입력
numbers = list(map(int, sys.stdin.readline().split(' ')))

# step3. 가장 가까운 3개의 숫자합을 출력
sum_number = 0
for x in numbers:
    for y in numbers[numbers.index(x)+1:]:
        for z in numbers[numbers.index(y)+1:]:
            if sum_number<x+y+z and x+y+z<=M:
                sum_number = x+y+z

print(sum_number)
    
