# 상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를
#   하게 사용하기 위해서 사용.

# 클래스 변수 
# : 인스턴스들이 모두 공유하는 그 클래스 공유의 변수
# 예) 부장님이 몬스터가 너무 많이 풀리면 서버 메모리에 문제가 있을 수 있으니 1000마리 정도로 최대 몬스터 제한을 걸어두자라고 했다
#     이런 경우 이것을 '클래스 변수'로 만들어 주어야 한다. (최대 몬스터 제한 수인 'max_num'>> Monster.max_num


import random
# 부모 클래스
class Monster:
    max_num = 1000                  # 클래스 변수, 특징: 변수 앞에 'self.'을 사용하지 않는다. 
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1        # 클래스 변수 제어, 이제 print(wolf.max_num) 등이 있는 줄들로 가서 변화를 보도록 하자.(다른 Skark, Dragon 클래스도 클래스 변수를 공유하는지 확인하기)
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):     # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)  # 부모클래스의 생성자(__init__) 속성값 가져오기
        self.skills = ("불품기", "꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")


wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)     # 몬스터 wolf가 하나 생성되었으므로 몬스터 수 최대 제한인 1000에서 1개가 줄어 999가 출력된다. 

shark = Shark("샤크", 3000, 400)
shark.move()
print(shark.max_num)    # 몬스터가 wolf, shark가 생성되었으므로 1000-2인 998이 출력된다. 

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
dragon.skill()
print(dragon.max_num)   # 몬스터가 wolf, shark, dragon이 생성되었으므로 1000-3인 997이 출력된다. 
