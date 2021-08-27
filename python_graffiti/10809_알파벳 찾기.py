# 문자열 
# 백준 - 10809번

import sys 

S = sys.stdin.readline()

# ASCII CODE를 활용하여 등장 횟수 세기
# ASCII CODE: a(97) ~ z(122) >> 0~25
alpha_seq = []
for alpha in range(26):
    count = 0
    for i in range(len(S)):
        if (chr(alpha+97)) == S[i]:
            alpha_seq.append(S.index(S[i]))
            break
        count += 1
        if count == len(S):
            alpha_seq.append(-1)
# 결과 출력
for alpha in alpha_seq:
    print(alpha, end=' ')