from tkinter import *
import time

# class Sprite
# : 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.
# 'sprite'의 의미 - 
class Sprite:
    def __init__(self, image, x, y):
        self.img = image    # 스프라이트가 가지고 있는 이미지
        self.x = x          # 현재 위치의 x좌표
        self.y = y          # 현재 위치의 y좌표
        self.dx = 0         # 단위시간에 움직이는 x방향 거리 
        self.dy = 0         # 단위시간에 움직이는 y방향 거리

    # 스프라이트의 가로 길이 반환
    def getWidth(self):
        return self.img.width()

    # 스프라이트의 세로 길이 반환
    def getHeight(self):
        return self.img.height()

    # 스프라이트를 화면에 그리기 
    def draw(self, g):
        g.create_image(self.x, self.y, anchor=NW, image=self.img)

    # 스프라이트를 움직이는 메소드
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # dx를 설정하는 설정자 메소드
    def setDx(self, dx):
        self.dx = dx

    # dy를 설정하는 설정자 메소드
    def setDy(self, dy):
        self.dy = dy
    
    # dx를 반환하는 접근자 메소드 
    def getDx(self):
        return self.dx
    
    # dy를 반환하는 접근자 메소드
    def getDy(self):
        return self.dy
    
    # x를 반환하는 접근자 메소드
    def getX(self):
        return self.x
    
    # y를 반환하는 접근자 메소드
    def getY(self):
        return self.y

    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다. 
    def checkCollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getWidth()
        p2y = self.y + self.getHeight()
        
        p3x = other.x
        p3y = other.y
        p4x = other.x + self.getWidth()
        p4y = other.y + self.getHeight()

        overlapped = not( p4x < p1x or      # () 안의 조건식은 겹치지 않을 조건이다. 네모를 그리고 좌하단 꼭짓점을 (p1x,p1y)라고 하자.
            p3x > p2x or                    # p4x < p1x: self와 겹치지 않게 other이 좌측이 위치 
            p2y < p3y or                    # p3x > p1x: self와 겹치지 않게 other이 우측에 위치 
            p1y > p4y)
        return overlapped

    # 충돌 처리한다. Sprite class에서는 아무 기능이 없으나, 자식 클래스에 오버라이드 된다. 
    def handleCollision(self,other):
        pass


# class StarShipSprite 
# : 우주선(StarShip)을 나타내는 클래스
class StarShipSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 0

    # 우주선을 움직이는 메서드. (윈도우 경계를 넘으려고 할 경우, 움직이지 못하게 할 것)
    def move(self):
        if ((self.dx < 0) and (self.x < 10)):
            return 
        if ((self.dy > 0) and (self.y < 10)):
            return 
        super().move()
        self.dx = 0

    # 충돌을 처리한다. 외계인 우주선과 충돌하면 게임이 종료되도록 한다. 
    def handleCollision(self, other):
        if type(other) is AlienSprite:
            self.game.endGame()


# class AlienSprite 
# : 외계인 우주선을 나타내는 클래스 
class AlienSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -10

    # 외게인 우주선을 움직이는 메소드(윈도우의 경계에 도달하면 한 칸 아래로 이동한다.)
    def move(self):
        if (((self.dx < 0) and (self.x <10)) or ((self.dx > 0) and (self.x > 750))):
            self.dx = -self.dx
            self.y += 50
            if self.y > 600:
                self.game.endGame()
            super.move()


# class ShotSprite
# : 포탄을 나타내는 클래스 
class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super.__init__(image, x, y)
        self.game = game
        self.dy = -20

    # 화면을 벗어나면 객체를 리스트에서 삭제한다. 
    def move(self):
        super().move()
        if self.y < -100:
            self.game.removeSprite(self)

    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다. 
    def handleCollision(self, other):
        if type(other) is AlienSprite:
            self.game.removeSprite(self)
            self.game.revmoeSprite(other)


# 갤러그 게임을 나타내는 클래스 
class GalagaGame():

    # "이벤트" 관련 매서드들
    # → 화살표 키 이벤트 처리
    def keyLeft(self, event):
        self.starship.setDx(+10)
        return

    # ← 화살표 키 이벤트 처리
    
    # 스페이스 키 이벤트를 처리

    
    # 게임에 필요한 스프라이트-를 생성
    

    # 생성자 메서드

    # 게임을 시작

    # 게임 종료

    # 스프라이틀르 리스트에서 삭제

    # 포탄 발사

    # 화면 그리기 

    # 게임 루프 
