'''
本節文章
https://learnscript.net/zh-hant/python/advanced/implementing-method-overriding/ 如何實作方法覆寫
'''

###
class Unit:
    # 類別 Unit，表示遊戲中的單位

    def __init__(self, hp, power):
        # 表示生命值和力量值的欄位
        self.hp = hp
        self.power = power

    def show_status(self):
        # 顯示單位的相關狀態
        print(f'單位狀態，生命值 {self.hp}，力量值 {self.power}')

###
class Hero(Unit):
    # 類別 Hero，表示玩家控製的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的欄位 name
        self.name = name

    def show_status(self):
        # 覆寫 Unit 類別的 show_status 方法
        # 通過 super() 呼叫 Unit 的 show_status，顯示生命值和力量值
        super().show_status()
        print(f'英雄名 {self.name}')

###
hero_name = input('請輸入英雄的名字：')

### 分別建立 Hero 類別和 Unit 類別的執行個體
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

### hero，enemy 將以不同的方式來顯示狀態
print('hero 顯示狀態')
hero.show_status()
print('enemy 顯示狀態')
enemy.show_status()
