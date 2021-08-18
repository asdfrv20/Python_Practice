# 문자열 
# 백준 - 1157번
# 참고: ASCII code A~Z(65~90, 26개), a~z(97~122, 26개)
# A(65), a(97)이므로 같은 대소문자의 차이는 32

import sys 

word = sys.stdin.readline()
word = word[:-1]

# 자리 수 세고 리스트에 저장하기 
alpha_count = []
for alpha in range(26):
    count = 0
    count += word.count(chr(alpha+65))
    count += word.count(chr(alpha+97))
    alpha_count.append(count)
# print('alpha_count: ', alpha_count)
# print(len(alpha_count))

# 출력
if alpha_count.count(max(alpha_count)) != 1:    # 가장 많이 사용된 알파벳이 여러개 존재하는 경우
    print('?')
else:                                           # 가장 많이 사용된 알파벳이 1개 존재하는 경우 
    print(chr(alpha_count.index(max(alpha_count))+65))