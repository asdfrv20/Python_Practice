# 실습문제 6.1.3
# 로또 번호 추출기 
# - 조건
# 1. 로또 번호 6개를 생성한다. 
# 2. 로또 번호는 1~45까지의 랜던한 번호다.
# 3. 6개의 숫자 모두 달라야 한다. 
# 4. getRandomNumber() 함수를 사용해서 구현한다.(random 모듈의 sample 함수는 사용하지 않는다.)

# my answer
import random

def getRandomNumber():
    number = random.randint(1,45)
    return number 

lotto_numbers = []  # 로또 번호를 저장할 리스트
while True:
    lotto_number = getRandomNumber()
    if lotto_number not in lotto_numbers:
        lotto_numbers.append(lotto_number)

    if len(lotto_numbers) == 6:
        lotto_numbers.sort()
        for num in lotto_numbers:
            print(num, end=' ')
        break 
    
# lecture solution
import random
def getRandomNumber():
    number = random.randint(1,45)
    return number 

lotto_num = []  # 로또 번호를 저장할 리스트

count = 0       # 현재 뽑은 숫자 개수 

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()
for num in lotto_num:
    print(num, end=' ')