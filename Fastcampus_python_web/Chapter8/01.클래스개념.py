# 클래스를 사용하는 이유 

champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

# 여기에서 Chapion 하나를 더 추가해 준다고 가정하자: 야스오 만들어 주기
champion3_name = "야스오"
champion3_health = 750
champion3_attack = 92

print(f"{champion2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

print("=========클래스를 사용한 경우==========")

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신 것을 환영합니다.")
    def basic_attack(self):
        print(f'{self.name} 기본공격 {self.attack}')

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 750, 92)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()
# class를 사용한 경우 역시 Chapion 하나를 더 추가: 야스오
# class를 사용하지 않은 경우와 비교했을 때 