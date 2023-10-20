'''
本节文章
https://learnscript.net/zh/python/senior/define-class-private-members/ 如何定义类的私有成员
'''

###
class Unit:
    # 类 Unit，表示游戏中的单位

    def __init__(self, hp, power):
        # 生命值
        # self.hp = hp
        self.__hp = hp
        # 力量值
        self.power = power

    def __hurt():
        # 私有方法 hurt，表示单位受伤了
        print('怎么？这就受伤了？')

###
class Hero(Unit):
    # 类 Hero，表示玩家控制的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的字段 name
        self.name = name

        # 访问继承自 Unit 类的 hp，power 字段
        # print(f'{self.name} 生命值：{self.hp} 攻击力：{self.power}')
        print(f'{self.name} 攻击力：{self.power}')

### 创建 Hero 类的实例
hero = Hero(100, 10, '钢铁侠')

# 访问字段 hp
# hero.hp += 100
# print(f'目前生命值为 {hero.hp}')

# ERROR __hurt 没有定义
# hero.__hurt()