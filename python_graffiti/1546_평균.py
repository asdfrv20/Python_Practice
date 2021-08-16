# 1차원 배열 
# 백준 - 1546번

import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

# 새로운 점수들 설정
M = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i]/M*100

# 평균 출력
average = sum(scores)/N
print(average)
