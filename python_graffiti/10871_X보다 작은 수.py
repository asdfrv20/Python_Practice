# for문
# 백준_10871번

import sys

N, X = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))

result = []
for i in range(len(A)):
    if A[i] < X:
        result.append(A[i])

for i in range(len(result)):
    print(result[i], end=' ')
