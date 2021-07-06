# 실습문제 5.3.3
# 한국어 연습 프로그램 작성
# -Learning Korean-
# 1. 연습할 한국어가 담긴 리스트를 만든다. 
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다 
# 3. 프로그램 사용자는 단어를 그대로 입려하고 
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료 
 
# my code
print("Let's Learning Korean")
for word in ['사랑해', '귀엽다', '고마워', '행복해']:
    print(word)
    answer = input("")
    if word != answer:
        break

# lecture answer
word_list = ['사랑해', '귀엽다', '고마워', '행복해']

print("Let's Learning Korean")
for word in word_list:
    print(word)
    data = input()
    if word != data:
        break