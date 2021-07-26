import math
import sys
import time

A, B, V = map(int, sys.stdin.readline().split())

start = time.time()

result = 1 + math.ceil((V-A)/(A-B))

print(result)
print("time: ",  time.time()-start)


# 내가 짠 코드 
import math
import time

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]

result = 1 + math.ceil((V-A)/(A-B))

print(result)
print("time: ", time.time()-start)