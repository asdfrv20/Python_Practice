# keyboard로 드론 움직이기 

from time import sleep
from e_drone.drone import *
import keyboard 

drone = Drone()
drone.open("COM6")

while(True):
    if keyboard.is_pressed("1"):    # 이륙
        print("TakeOff")
        drone.sendTakeOff()
        sleep(0.2)
        drone.sendControlWhile(0,0,0,0,3000)
    if keyboard.is_pressed("2"):    # 착륙
        print("Landing")
        drone.sendLanding()
        sleep(0.2)
        drone.sendLanding()
        sleep(0.2)
    if keyboard.is_pressed("space"):
        print("stop")
        drone.sendControlWhile(0,0,0,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("w"):    # 앞으로
        print("Forward")
        drone.sendControlWhile(0,25,0,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("s"):    # 뒤로 
        print("Back")
        drone.sendControlWhile(0,-25,0,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("a"):    # 왼쪽으로 
        print("Left")
        drone.sendControlWhile(-25,0,0,0,1000)
        sleep(0.2)    
    if keyboard.is_pressed("d"):    # 오른쪽으로 
        print("Right")
        drone.sendControlWhile(25,0,0,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("q"):    # 상승
        print("Up")
        drone.sendControlWhile(0,-0,0,25,1000)
        sleep(0.2)
    if keyboard.is_pressed("e"):    # 하강
        print("Down")
        drone.sendControlWhile(0,0,0,-25,1000)
        sleep(0.2)
    if keyboard.is_pressed("o"):    # 좌회전  
        print("Turn Left")
        drone.sendControlWhile(0,0,-25,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("p"):    # 우회전 
        print("Turn Right")
        drone.sendControlWhile(0,0,25,0,1000)
        sleep(0.2)
    if keyboard.is_pressed("up"):
        print("Forward Flip")
        drone.sendFlightEvent(FlightEvent.FlipFront)
        sleep(0.2)
    if keyboard.is_pressed("down"):
        print("Rear Flip")
        drone.sendFlightEvent(FlightEvent.FlipRear)
        sleep(0.2)
    if keyboard.is_pressed("left"):
        print("Left Flip")
        drone.sendFlightEvent(FlightEvent.FlipLeft)
        sleep(0.2)
    if keyboard.is_pressed("right"):
        print("Right Flip")
        drone.sendFlightEvent(FlightEvent.FlipRight)
        sleep(0.2)
    



