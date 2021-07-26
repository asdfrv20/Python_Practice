# 내장 모듈
# : 파이썬 설치 시 자동으로 설치되는 모듈


import math 
print(math.pi)
print(math.ceil(5.7))

from math import pi, ceil
print(pi)
print(ceil(5.7))

from math import pi, ceil as c
print(pi)
print(c(5.7))


# 외부 모듈
# : 다른 사람들이 만든 파이썬 파일 pip로 설치해서 사용 
# pyautogui (url: https://pyautogui.readthedocs.io/en/latest/)

# import pyautogui as pg   # 마우스나 키보드를 자동으로 이동시키는 매크로 모듈
# pg.moveTo(500,500, duration=2)

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')