'''
本節文章
https://learnscript.net/zh-hant/python/advanced/generate-random-numbers/ 如何產生隨機亂數
'''

### 匯入 random 模組
import random

# 使用 randint 取得隨機整數
num1 = random.randint(0, 10)
# 使用 random 取得隨機浮點數
num2 = random.random()

print(f'隨機整數：{num1}')
print(f'隨機浮點數：{num2}')

class Unit:
    # 類別 Unit，表示遊戲中的單位

    def __init__(self, hp, power):
        # 表示生命值和力量值的欄位
        self.hp = hp
        self.power = power

    def show_status(self):
        # 顯示單位的相關狀態
        print(f'單位狀態，生命值 {self.hp}')

    def attack(self, target):
        # 方法 attack 用來攻擊另一個遊戲單位

        # 通過 randint 產生一個隨機的傷害值
        damage = self.power + random.randint(-10, 10)

        # 根據傷害值減少生命值，小於等於 0 傳回 True，表示單位被擊敗
        target.hp -= damage
        print(f'受到 {damage} 點傷害')

        if target.hp <= 0:
            return True

###
class Hero(Unit):
    # 類別 Hero，表示玩家控製的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的欄位 name
        self.name = name

    def show_status(self):
        # 顯示英雄的相關狀態
        print(f'英雄名 {self.name}，生命值 {self.hp}')

###
hero_name = input('請輸入英雄的名字：')

### 分別建立 Hero 類別和 Unit 類別的執行個體
hero = Hero(40, 10, hero_name)
enemy = Unit(40, 10)

# 顯示英雄和敵人的初始狀態
hero.show_status()
enemy.show_status()

# 讓英雄和敵人相互攻擊，直到其中一方死亡
while True:
    # 英雄首先攻擊敵人
    if hero.attack(enemy):
        print('英雄勝利')
        break
    else:
        # 如果敵人還活著，則顯示他的狀態
        enemy.show_status()

    # 敵人攻擊英雄
    if enemy.attack(hero):
        print('英雄陣亡')
        break
    else:
        # 如果英雄還活著，則顯示他的狀態
        hero.show_status()
