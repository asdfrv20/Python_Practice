# 터렛 
# 백준 - 1002번 

import sys
import math

# 입력
T = int(sys.stdin.readline())
pos1 = []
pos2 = []
for i in range(T):
    temp = list(map(int, sys.stdin.readline().split(' ')))
    pos1.append(temp[0:3])
    pos2.append(temp[3:])

# 마린이 있을 수 있는 예상 위치 수 계산
for i in range(T):
    dist_xy = math.sqrt((pos1[i][0]-pos2[i][0])**2 + (pos1[i][1]-pos2[i][1])**2)
    dist_rr_sub = abs(pos1[i][2] - pos2[i][2])
    dist_rr_add = pos1[i][2] + pos2[i][2]

    # 두 점의 위치 관계에 따른 경우 나누기 
    # 일치(-1)
    if pos1[i][0] == pos2[i][0] and pos1[i][1] == pos2[i][1] and pos1[i][2] == pos2[i][2]:
        possible_pos = -1
    # 한점 일치(1)
    elif dist_xy == dist_rr_sub or dist_xy == dist_rr_add:
        possible_pos = 1
    # 일치 X(0)
    elif dist_xy < dist_rr_sub or dist_xy > dist_rr_add:
        possible_pos = 0
    else:
        possible_pos = 2

    print(possible_pos)



