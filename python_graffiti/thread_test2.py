# DeadLock problem을 보여주는 예제
# ※ DeadLock Problem: 하나의 자원(예를 들어 변수라고 하자)을 여러 스레드가 공유하여 
#    원하는 명령을 전부 수행하지 못하고 곱창난 상황을 말한다. 

import threading
 
# CounterThread
class CounterThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='Timer Thread')
 
    # CounterThread가 실행하는 함수
    def run(self):
        global totalCount
 
        # 2,500,000번 카운트 시작
        for _ in range(2500000):
            totalCount += 1
        print('2,500,000번 카운팅 끝!')
 
if __name__ == '__main__':
    # 전역 변수로 totalCount를 선언
    global totalCount
    totalCount = 0
 
    # totalCount를 1씩 더하는 
    # Counter Thread를 4개 만들어서 동작시킨다.
    for _ in range(4):
        timerThread = CounterThread()
        timerThread.start()
 
    print('모든 Thread들이 종료될 때까지 기다린다.')
    mainThread = threading.currentThread()
    for thread in threading.enumerate():
        # Main Thread를 제외한 모든 Thread들이 
        # 카운팅을 완료하고 끝날 때 까지 기다린다.
        if thread is not mainThread:
            thread.join()
 
    print('totalCount = ' + str(totalCount))