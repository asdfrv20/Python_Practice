# Deadlock problem 을 "Event 방식"을 해결한 예제
'''
[DeadLock problem을 해결하기 위한 방법]
1. Event 방식(Flag 방식)
2. key를 하나만 주는 방식
3. key를 여러 개 주는 방식
4. 파생2
'''

import threading

from queue import Queue


def creator(data, q):
    """
    생산자 : 쓰레드간 데이터 전송 예제
    """
    print('Creating data and putting it on the queue')
    print('\n')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
        print('Waiting for data to be doubled')
        evt.wait()


def consumer(q):
    """
    소비자 : 쓰레드간 데이터 전송 예제
    """
    while True:
        data, evt = q.get()
        print('Receive Original Data : {}'.format(data))
        processed = data * 5
        print('Receive Processed Data : {}'.format(processed))
        print('\n')
        evt.set()
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    data = [3.6, 30.4, 3.6, 3.6, 2.0, 9.8, 33.6, -20.6, 30.4]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=consumer, args=(q,))
    thread_one.start()
    thread_two.start()

    q.join()