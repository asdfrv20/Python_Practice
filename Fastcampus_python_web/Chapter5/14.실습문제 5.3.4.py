# 실습문제 5.3.4
# 실습문제 5.3.3의 업그레이드 버전
# list의 문제를 맞추고 마지막에 '전체 문재 개수, 맞힌 문제 개수, 틀린 문제 개수'를 출력하는 함수 

word_list = ['사랑해', '귀엽다', '고마워', '행복해']

print("Let's Leanring Korean")
score = 0
for word in word_list:
    print(word)
    data = input()
    if word == data:
        score += 1

print("전체 문제 개수:", len(word_list))
print("맞힌 문제 개수:", score)
print("틀린 문제 개수:", len(word_list)-score)