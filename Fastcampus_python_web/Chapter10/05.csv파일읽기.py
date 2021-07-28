import csv

file = open("./Fastcampus_python_web/Chapter10/student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()