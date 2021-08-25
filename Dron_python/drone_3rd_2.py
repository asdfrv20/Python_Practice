# 군집 드론 제어 

import time
from e_drone.drone import *

drone1 = Drone()
drone2 = Drone()

drone1.open("COM6")
drone2.open("COM7")

drone1.sendTakeOff()        # drone1 이륙
time.sleep(0.1)
drone2.sendTakeOff()        # drone2 이륙
time.sleep(0.01)

# 5초 동안 호버링
drone1.sendControlWhile(0,0,0,0,2000)
drone2.sendControlWhile(0,0,0,0,2000)

# 이동하기 
drone1.sendControlWhile(0,50,0,0,1000)
drone2.sendControlWhile(0,-50,0,0,1000)

# 1초 동안 정지하기 
drone1.sendControlWhile(0,0,0,0,1000)
drone2.sendControlWhile(0,0,0,0,1000)

drone1.sendLanding()        # 착륙
drone2.sendLanding()
time.sleep(0.01)

drone1.sendLanding()
drone2.sendLanding()
time.sleep(0.01)

drone1.close()
drone2.close()

