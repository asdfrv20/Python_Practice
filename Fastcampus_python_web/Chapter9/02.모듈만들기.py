import pay_module

# 변수 사용 
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2021-07-26")
print(pay_info.get_pay_info())

# pay_module의 __name__ 확인하기 
print(pay_module.__name__)