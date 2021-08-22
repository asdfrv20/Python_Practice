# 1차원 배열
# 백준 - 8958번
# ※ 어려움: 연속되는 정답(O)의 점수를 어떤 식으로 더해 줄 것인가

import sys

T = int(sys.stdin.readline())

# 정오표 읽어오기 
errata = []
for i in range(T):
    temp = sys.stdin.readline()
    temp = temp[:-1]
    errata.append(temp)
# print(errata)

# X를 기준으로 분할 후, 점수 계산
scores = []
for i in range(len(errata)):
    errata[i] = errata[i].split('X')        # X를 기준으로 나누기 
    cnt_O = []                              # 연속된 O의 개수들을 세어 cnt_O에 저장
    for j in range(len(errata[i])):
        cnt_O.append(errata[i][j].count('O'))
    
    score = 0 
    for k in range(len(cnt_O)):             # 점수 계산: 연속된 n개 만큼 1에서 n까지 더하는 과정 반복                          
        if cnt_O[k] == 0:                   # cnt_O가 0인 경우, continue로 넘어가기
            continue
        else:                               # cnt_O가 0이 아닌 경우, 1에서 cnt_O[k]까지 더하기 
            for l in range(1, cnt_O[k]+1):
                score += l
    scores.append(score)

    # print(f"errata[{i}]:", errata[i])
    # print(f"cnt_O[{i}]:", cnt_O)
    print(scores[i])

