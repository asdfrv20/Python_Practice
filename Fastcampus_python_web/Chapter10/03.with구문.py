# with 구문을 활용하여 파일 읽어오기

with open("./Fastcampus_python_web/Chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)