# 실습문제 5.2.2
# 턱걸이 횟수를 저장할 빈 리스트를 만든 후 
# 일주일간의 턱걸이 횟수를 입력받아 리스트에 저장

pull_up = []        # 빈 리스트 생성
temp = int(input("1일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("2일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("3일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("4일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("5일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("6일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
temp = int(input("7일차 턱걸이 횟수 >>> "))
pull_up.append(temp)
print(pull_up)

# 내 답안(너무 답답해서 for문을 활용해서 구현)
sum = 0
for i in pull_up:
    sum += i
avg = sum/len(pull_up)
print(avg)

# 답안
total = pull_up[0] + pull_up[1] + pull_up[2] + pull_up[3] \
        + pull_up[4] + pull_up[5] + pull_up[6]
average = total/7

print(average)

# for문 답안
for i in range(1, 101):
    x = int(input(i, "일차 턱걸이 횟수"))
    pull_up.append(x)