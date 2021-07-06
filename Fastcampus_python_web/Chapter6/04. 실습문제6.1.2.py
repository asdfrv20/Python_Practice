# 실습문제 6.1.2
# : 세 개의 정수를 인자로 받아, 합계와 평균을 출력하는 함수, printSumAvg(x,y,z)를 함수로 정의해보자 

# Tip) 문자열 포매팅 
def printSumAvg(x,y,z):
    '''
    세 개의 정수를 인자로 받아, 합계와 평균을 출력하는 함수
    '''
    sum = x+y+z
    avg = sum/3
    # print('합계:',sum, '평균:', avg)
    print(f"합계: {sum}, 평균: {avg}")

printSumAvg(100,256,700)