# 실습문제 10.1.1


# my solve
import csv

# [주식데이터를 불러와 비교 후 수익금과 수익률 출력]
# step1. 주식의 현재가 입력(변화)
cur_price = [
    ["종목", "현재가"],
    ["삼성전자", 0],
    ["NAVER", 0]
]
for i in range(1, len(cur_price)):
    cur_price[i][1] = int(input(f"{cur_price[i][0]} 주식 현재가>> "))

# step2. mystock.csv로 부터 주식 데이터 가져오기 
file2 = open("./Fastcampus_python_web/Chapter10/mystock.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file2)
my_stock = []
for date in reader:
    my_stock.append(date)
file2.close()

# step3.my_stock 데이터 형변환
for i in range(1,len(my_stock)):
    for j in range(1,len(my_stock[i])):
        my_stock[i][j] = int(my_stock[i][j])

for i in range(len(my_stock)):
    print(my_stock[i])

# step4.목표가 도달 시 '수익금&수익률' 출력
for i in range(1, len(my_stock)):
    if cur_price[i][1] >= my_stock[i][3]:
        proceeds = (my_stock[i][3]-my_stock[i][1])*my_stock[i][2]
        stock_yield = (my_stock[i][3]/my_stock[i][1]-1)*100
        print("%s %d %0.2f%%" %(my_stock[i][0], proceeds, stock_yield))


# 강의 내용
# 오류 해결 과정 중심!!

import csv

# 함수로 만들어 가독성을 높인다. 
def show_profit(data):
    name = data[0]  # 종목
    purchase_price = int(data[1])   # 매입가
    amount = int(data[2])   # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount   # 수익금
    profit_ratio = (target_price / purchase_price - 1) * 100    # 수익률
    
    print(f"{name} {profit} {profit_ratio:.2f}%")

# 파일 열기
file = open("./Fastcampus_python_web/Chapter10/mystock.csv", "r", encoding="utf-8-sig")

# 파일 데이터 읽기
reader = list(csv.reader(file))
for data in reader[1:]:     # 1행의 정보는 필요 없기 때문에 슬라이싱으로 처리해주어 제외시고자 함 BUT 오류뜸. >> reader 객체를 list로 형변환 시키기
    show_profit(data)
file.close()


# my solve RE

