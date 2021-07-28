import csv

data = [
    ["이름", "반", "번호"], 
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 32]
]

# [아래 open 명령의 속성 설명]
# newline="": windows에서 csv파일 생성 시, 한 줄 씩 자동으로 띄어주는 것을 방지하기 위한 속성
# encoding="utf-8-sig": 한글이 깨지는 것을 방지한 encoding
file = open("./Fastcampus_python_web/Chapter10/student.csv", 'w', newline="", encoding="utf-8-sig")      
writer = csv.writer(file)   # .txt 와는 명령이 다름에 주의
for d in data:
    writer.writerow(d)      # list로 작성된 data가 한 줄 씩 writer에 csv파일에 저장되게 된다.
file.close()
