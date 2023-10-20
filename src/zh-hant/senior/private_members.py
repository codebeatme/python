'''
本節文章
https://learnscript.net/zh-hant/python/senior/define-class-private-members/ 如何定義類別的私用成員
'''

###
class Unit:
    # 類別 Unit，表示遊戲中的單位

    def __init__(self, hp, power):
        # 生命值
        # self.hp = hp
        self.__hp = hp
        # 力量值
        self.power = power

    def __hurt():
        # 私用方法 hurt，表示單位受傷了
        print('怎麽？這就受傷了？')

###
class Hero(Unit):
    # 類別 Hero，表示玩家控製的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的欄位 name
        self.name = name

        # 存取繼承自 Unit 類別的 hp，power 欄位
        # print(f'{self.name} 生命值：{self.hp} 攻擊力：{self.power}')
        print(f'{self.name} 攻擊力：{self.power}')

### 建立 Hero 類別的執行個體
hero = Hero(100, 10, '鋼鐵俠')

# 存取欄位 hp
# hero.hp += 100
# print(f'目前生命值為 {hero.hp}')

# ERROR __hurt 沒有定義
# hero.__hurt()