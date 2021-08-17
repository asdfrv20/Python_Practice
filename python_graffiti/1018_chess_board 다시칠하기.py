# - 체스판 다시 칠하기
# BAEKJOON - 1018번
# feat. 아이디어제공: 영진좌

import sys
import copy
import time

case_W = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

case_B = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

# 1. 입력 받기
N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    temp = input()
    board.append(temp)
# print(len(board))
# print(board, type(board))

start = time.time()

# 2.체스판 패턴이 가장 많이 나타나는 부분 찾기
least_paint = 64

## 체스판 후보 부분 자르기
for i in range(N-7):
    for j in range(M-7):
        # print("\n", i, j)
        dummy_board = [row[j:j+8] for row in board[i:i+8]]  # 매우 중요!!
        # print(dummy_board)

        # case1. 흰색 start인 경우와 떼어온 dummy_board와 비교 
        count=0
        for x in range(8):
            for y in range(8):
                if dummy_board[x][y] != case_W[x][y]:
                    count += 1
        if count < least_paint:
            least_paint = copy.copy(count)
        # print("least_paint(W): ", least_paint)
        x=0; y=0    # x,y 초기화

        # case2. 검은색 start인 경우와 떼어온 dummy_board와 비교
        count=0
        for x in range(8):
            for y in range(8):
                if dummy_board[x][y] != case_B[x][y]:
                    count += 1
        if count < least_paint:
            least_paint = copy.copy(count)
        # print("least_paint(B): ", least_paint)
        x=0; y=0

# 3. 출력
print(least_paint)
# print("time: ", time.time()-start)
