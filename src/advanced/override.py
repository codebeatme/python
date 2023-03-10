# 视频内容：「Python」进阶教程 方法重写有什么用？如何实现类的方法重写？使用super访问父类
# 视频地址：https://www.bilibili.com/video/BV1qg4y1J7y1/

###
class Unit:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def show_info(self):
        print(f'单位状态，生命值{self.hp}，攻击力{self.power}')

###
class Hero(Unit):

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        self.name = name

    def show_info(self):
        print(f'英雄{self.name}状态，生命值{self.hp}，攻击力{self.power}')

###
hero_name = input('请输入英雄的名字：')

###
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

hero.show_info()
enemy.show_info()
