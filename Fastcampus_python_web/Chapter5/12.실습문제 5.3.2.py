# 실습문제 5.3.2
# -과제-
# 숫자 1 입력: "게임을 시작합니다." 출력
# 숫자 2 입력: "실시간 랭킹" 출력
# 숫자 3 입력: "게임을 종료합니다." 출력 후 프로그램 종료

while True:
    print("[메뉴를 입력하세요]")
    choose = int(input("1.게임시작 2.랭킹보기 3.게임종료 >>> "))
    if choose<1 or choose>3:
        print("->다시 입력해주세요.")
    else:
        if choose==1:
            print("->게임을 시작합니다.")
        elif choose==2: 
            print("->실시간 랭킹")
        else:
            print("->게임을 종료합니다.")
            break