# 실습문제 5.1.4
# 사용자로부터 국어,영어,수학 성적을 입력받고 
# 세 과목의 평균 점수가 80점 이상이면 '불합격'이 표시되도록 프로그램을 출력해 보자 
# 이 때, 0~100점 사이의 숫자가 아닌 점수가 입려된 경우 '잘못 입려하셨습니다.'를 표시

kor = int(input("국어>>> "))
math = int(input("수학>>> "))
eng = int(input("영어>>> "))

# 내 답안
avg = (kor+math+eng)/3

if (kor<0 or kor>100) or (math<0 or math>100) or (eng<0 or eng>100):
    print("잘못 입력하셨습니다.")
elif avg>=80:
    print("불합격")
else:
    print("합격")

# 방법 1: 이중 조건문 활용하기 
if 0 <= kor <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else: 
    print("잘못 입력하셨습니다.")

# 방법2
if kor < 0 or kor > 100 or math < 0 or math > 100 or eng < 0 eng > 100:
    print("잘못 입력하셨습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")