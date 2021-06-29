# 1.리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치", "벼메뚜기", "비단뱀", "도롱뇽"]

# - 데이터가 없는 리스트
empty = []

# 2. 리스트 조작하기 

# - 데이터 접근하기
# 인덱스는 0부터 시작 
print(animals[2])
print(animals[-1])      # 가장 마지막 데이터를 반환하는 index: -1

# - 데이터 추가하기
animals.append("고라니")
print(animals)

# - 데이터 할당하기: 벼메뚜기>청개구리
animals[1] = "청개구리"
print(animals)

# - 데이터 삭제: 가물치 삭제하기 
del animals[0]
print(animals)

# - 리스트 슬라이싱
print(animals[1:3])
print(animals[:])       # 전체다 가져오기 
print(animals[:3])      # 시작 index 생략하기, 0~2까지
print(animals[1:])      # 끝 index 생략하기, 1~끝까지

# - 리스트 길이
print(len(animals))

# - 리스트 정렬
animals.sort()      # 사전 순서대로 정렬(오름차순)
print(animals)
animals.sort(reverse=True)     # 사전 역순으로 정렬(내림차순)
print(animals)
