# 브루트 포스
# 백준 - 2231번

import copy

N = int(input())

# N의 가장 작은 생성자를 구하는 알고리즘 
result = N
temp = 0
for number in range(N):
    dummy = copy.copy(number)
    split_numbers = []
    while dummy >= 10:
        split_numbers.append(dummy%10)
        dummy = dummy//10
    split_numbers.append(dummy)
    
    # 생성자 후보의 분해합 구한 후, 최솟값일 때 대입
    temp = number+sum(split_numbers)
    if N == temp and number<result:
         result = number
if result == N:
    result = 0

print(result)