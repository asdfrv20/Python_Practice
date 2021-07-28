# 1. 파일 쓰기 
file = open("./Fastcampus_python_web/Chapter10/data.txt", "w", encoding="utf8")        # 파일 열기
file.write("1. 스타트코딩과 함께 파이썬 공부")  # 파일 작업
file.close()                                    # 파일 닫기 

# 2. 파일 추가하기 
file = open("./Fastcampus_python_web/Chapter10/data.txt", "a", encoding="utf8")
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()

# 3. 파일 읽기
file = open("./Fastcampus_python_web/Chapter10/data.txt", "r", encoding="utf8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
# : 파일이 언제가 마지막인지 알 수 있도록 만들어 주는 로직을 적용해야 한다.
while True:
    data = file.readline()  # 한줄씩 데이터 읽어오기
    print(data, end="")
    if data == "":          # .readline()이 공백문자("")가 되는 경우 == 파일의 끝이 되는 경우
        break
file.close()