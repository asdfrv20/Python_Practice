# 새로운 Error 정의하기
class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력불가")

try:
    num = int(input("음수를 입력해주세요>>> "))
    if num >= 0:
        raise ValueError("양수는 입력 불가")
except PositiveNumberError as e:
    print("에러 발생!", e)