# 실습문제 5.2.1
# 다음은 1번~5번 학생의 1분간 팔굽혀펴기 개수이다 
push_up = [33, 40, 12, 63, 52]

# 문항1: 6번의 팔굽혀펴기 개수 9개 추가하기
push_up.append(9)
print(push_up)

# 문항2: 2번의 재측정 결과 50개를 하여 데이터 수정
push_up[2] = 50
print(push_up)

# 문항3: 3~6번까지의 데이터 슬라이싱 
temp = push_up[3:]
print(temp)

# 문항4: 모든 데이터를 오름차순으로 정렬
push_up.sort()
print(push_up)