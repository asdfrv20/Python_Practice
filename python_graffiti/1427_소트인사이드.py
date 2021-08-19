# 정렬
# 백준 - 1427번

import sys 

# 문자열 받기
word = sys.stdin.readline()
word = word[:-1]

# 한 자리씩 문자열로 바꾸기 
word_list = []
for i in range(len(word)):
    word_list.append(word[i])

word_list.sort(reverse = True)
for i in range(len(word)):
    print(word_list[i], end='')


# python 1위 답안
print(''.join(sorted(input())[ : :-1]))
