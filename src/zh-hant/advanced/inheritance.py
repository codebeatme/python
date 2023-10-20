'''
本節文章
https://learnscript.net/zh-hant/python/advanced/implementing-class-inheritance/ 如何實現類別的繼承
'''

###
class Unit:
    # 類別 Unit，表示遊戲中的單位

    def __init__(self, hp, power):
        # 表示生命值和力量值的欄位
        self.hp = hp
        self.power = power

###
class Hero(Unit):
    # 類別 Hero，繼承自 Unit，表示玩家控製的英雄

    def __init__(self, hp, power, name):
        # 通過 super() 來存取基礎類別 Unit 的建構方法
        super().__init__(hp, power)
        # 對比 Unit 類別，增加一個表示名字的欄位 name
        self.name = name

###
hero_name = input('請輸入英雄的名字：')

### 分別建立 Hero 類別和 Unit 類別的執行個體
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

print(f'玩家狀態，英雄 {hero.name}，生命值 {hero.hp}，力量值 {hero.power}')
print(f'敵人狀態，生命值 {enemy.hp}，力量值 {enemy.power}')
