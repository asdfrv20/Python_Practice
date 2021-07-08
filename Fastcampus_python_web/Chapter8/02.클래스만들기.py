class Monster:
    def __init__(self, name ,health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
    def say(self):
        print(f"나는 {self.name}(이)다!!")
    def info(self):
        print(f"체력:{self.health}/ 공격력:{self.attack}/ 이동속도:{self.speed}")
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

goblin = Monster('고블린',800,120,300)
wolf = Monster('울프',1500,200,350)
goblin.say()
goblin.info()
wolf.say()
goblin.info()

goblin.say()
goblin.decrease_health(50)
goblin.info()

# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열객체"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())      # .__dir__(): 해당 객체 안에 있는 메서드들을 확인할 수 명령