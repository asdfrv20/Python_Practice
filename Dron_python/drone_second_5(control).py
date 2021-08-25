import time
from e_drone.drone import *

drone = Drone()

drone.open("COM6")      # drone 통신 연결

print("TakeOff")
drone.sendTakeOff()     # 이륙 
time.sleep(0.1)         # 드론이 이륙할 시간 기다리기 

# 호버링
'''
drone.sendControlWhile(0, 0, 0, 0, 6000)       # (roll, pitch, yaw, throttle, timeMs)단위: ms
'''

# 사각형 그리기
'''
drone.sendControlWhile(35, -20, 0, 0, 700)
drone.sendControlWhile(-15, -20, 0, 0, 100)

drone.sendControlWhile(-15 ,-70, 0, 0, 700)
drone.sendControlWhile(-15, -20, 0, 0, 100)

drone.sendControlWhile(-65, -20, 0, 0, 700)
drone.sendControlWhile(-15, -20, 0, 0, 100)

drone.sendControlWhile(  -15, 30, 0, 0, 700)
drone.sendControlWhile(-15, -20, 0, 0, 100)
'''

# 지그재그로 이동하기 (yaw값 변형)
'''
drone.sendControlWhile(-15, -20, -30, 0, 600)
for i in range(2):
    drone.sendControlWhile(-15, 40, 0, 0, 1000)
    drone.sendControlWhile(-15, -20, 60, 0, 600)
    drone.sendControlWhile(-15, 40, 0, 0, 1000)
    drone.sendControlWhile(-15, -20, -60, 0, 600)
drone.sendControlWhile(-15, -20, 0, 30, 600)
drone.sendControlWhile(-15, -20, 0, 0, 1000)        # 마지막 호버링 
'''

# 드론 원형 패턴 비행(4초 정도 비행)
'''
drone.sendControlWhile(-15, -20, 0, 50, 1000)
drone.sendControlWhile(35, -20, -40, 0, 4000)
drone.sendControlWhile(-15, -20, 0, 0, 600)
drone.sendControlWhile(-65, -20, 50, 0, 4000)
drone.sendControlWhile(-15, -20, 0, 0, 600)
'''

#점점 더 커지는 원을 그리면서 비행하기 
'''
drone.sendControlWhile(0, 0, 0, 80, 4000)
roll = 0
yaw = 60
for i in range(3):
    drone.sendControlWhile(roll, 0, yaw, 50, 3000)
    roll += 30
    yaw -= 30
'''
# 위 아래로 소용돌이 
'''
drone.sendControlWhile(-15, -20, 0, 0, 600)       # 호버링
drone.sendControlWhile(0, 50, 50, 20, 5000)         # 상승
drone.sendControlWhile(0, 0, 0, 0, 600)
drone.sendControlWhile(0, -50, -50, -20, 5000)      # 하강
drone.sendControlWhile(0, 0, 0, 0, 600)
'''

# 왼쪽플립

drone.sendControlWhile(0,0,0,0, 3000)       # 호버링

drone.sendControlWhile(0,50,0,0 ,1000)      # 가속을 위한 시간 
time.sleep(1)

drone.sendFlightEvent(FlightEvent.FlipFront) #  플립하기 
time.sleep(2)
drone.sendControlWhile(0,0,0,0,3000)        # 플립 후 3초간 호버링 

drone.sendControlWhile(0,-50,0,0,1000)
time.sleep(1)
drone.sendFlightEvent(FlightEvent.FlipRear)
drone.sendControlWhile(0,0,0,0,3000)

print("Landing")
drone.sendLanding()     # 착륙(오류가 종종 발생하므로 2번 실행해주기 )
time.sleep(0.3)
drone.sendLanding()
time.sleep(0.3)

drone.close()           # drone 통신 끊기 

