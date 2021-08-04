# - 백준 7568번 덩치 문제

import sys
# import time

# 입력 가져오기 
N = int(input(""))
people = []
for i in range(N):
    height, weight = (sys.stdin.readline().split())
    height = int(height)
    weight = int(weight)
    temp = [height, weight, 1]
    people.append(temp)

# 순위 판단
# start = time.time()
for i in range(len(people)):
    for j in range(len(people)):
        if i == j:
            continue
        else:
            if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
                people[i][2] += 1
                

# 등수 출력
for i in range(len(people)):
    print(f"{people[i][2]}", end=" ")
# print("\ntime: ", time.time()-start)