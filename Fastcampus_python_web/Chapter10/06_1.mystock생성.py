import csv

# step0.(사전 작업) mystock.csv 데이터 저장하기 
stock_data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER", 380000, 5 ,400000]
]
# 나의 주식종목 정보(stock_data) csv파일로 저장
file = open("./Fastcampus_python_web/Chapter10/mystock.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)
for d in stock_data:
    writer.writerow(d)
file.close()

