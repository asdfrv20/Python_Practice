# 실습문제 8.1.1
# : 클래스 다이어그램을 보고 class를 만들어보자

# 아이템
class Item:
    Item_num = 1000
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def display_ItemInfo(self):
        print(f"<[{self.name}] 정보>")
        print(f"가격: {self.price}")
        print(f"무게: {self.weight}")
        print(f"버리기 가능여부: {self.isdropable}")
    def sale(self):
        print(f'[{self.name}]의 가격: {self.price}Gold')
        while True:
            sale_choose = int(input("물건을 판매하시겠습니까?(1.판매//2.취소)>>"))
            if sale_choose == 1:
                print(f"[{self.name}]의 판매가 완료되었습니다. {self.price}가 지급됩니다.")
            elif sale_choose == 2:
                print("거래가 취소되었습니다.")
            else: 
                print("잘못된 입력입니다.")   
            if sale_choose == 1 or sale_choose == 2:
                break
    def discard(self):
        while True:
            discard_choose = int(input("아이템을 버리시겠습니까?(1.버리기//2.취소)>>"))
            if not self.isdropable:
                print("버릴 수 없는 아이템 입니다.")
                break
            else:
                if discard_choose == 1:
                    print(f"[{self.name}]을 버립니다.")
                elif discard_choose == 2:
                    print("버리기를 취소합니다.")
                else:
                    print("잘못된 입력입니다.")
                if discard_choose == 1 or discard_choose == 2:
                    break

# 장비 아이템
class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        while True:
            wear_choose = int(input("장비를 착용합니까?(1.착용/2.취소)>> "))
            if wear_choose == 1:
                print(f"[{self.name}]을 착용하였습니다. 효과 '{self.effect}'이(가) 적용됩니다.")
            elif wear_choose == 2:
                print("취소되었습니다.")
            else:
                print("잘못된 입력입니다.") 
            if wear_choose == 1 or wear_choose == 2:
                break   

# 소모품 아이템
class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        while True:
            use_choose = int(input("아이템을 사용하시겠습니까?(1.사용/2.취소)>> "))
            if use_choose == 1:
                print(f"[{self.name}]을 사용합니다. 효과 '{self.effect}'이(가) 적용됩니다.")
            elif use_choose == 2:
                print("취소되었습니다.")
            else:
                print("잘못된 입력입니다.")
            if use_choose == 1 or use_choose == 2:
                break

# 객체 생성 
iron_armor = WearableItem("철갑옷", 2000, 40, True, "방어력+100")
iron_armor.display_ItemInfo()
iron_armor.wear()
iron_armor.sale()
iron_armor.discard()

flame_sword = WearableItem("플레임 소드", 5000, 5, False, "공격 시, 화염 속성 추가 데미지")
flame_sword.display_ItemInfo()
flame_sword.wear()
flame_sword.sale()
flame_sword.discard()

aqua_shoes = WearableItem("아쿠아슈즈", 4000, 3, True, "물 속성 내성")
aqua_shoes.display_ItemInfo()
aqua_shoes.wear()
aqua_shoes.sale()
aqua_shoes.discard()

raspberry = UsableItem("산딸기", 50, 0.1, True, "체력 50 증가")
raspberry.display_ItemInfo()
raspberry.use()
raspberry.sale()
raspberry.discard()

red_potion = UsableItem("빨간 포션", 100, 0.2, True, "체력 100 회복")
red_potion.display_ItemInfo()
red_potion.use()
red_potion.sale()
red_potion.discard()

blue_potion = UsableItem("파란 포션", 150, 0.2, True, "마력 150 회복")
blue_potion.display_ItemInfo()
blue_potion.use()
blue_potion.sale()
blue_potion.discard()

Goddess_Tear = UsableItem("여신의 눈물", 90000, 0.1, False, "30분 동안 파티원들의 모든 능력치가 80% 증가합니다.")
blue_potion.display_ItemInfo()
blue_potion.use()
blue_potion.sale()
blue_potion.discard()