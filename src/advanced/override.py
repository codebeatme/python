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