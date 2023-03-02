# 视频内容：「Python」进阶教程 如何生成随机数？random和randint区别
# 视频地址：https://www.bilibili.com/video/BV1J24y1V7XX/

###
import random

num1 = random.randint(0, 10)
num2 = random.random()

###
class Unit:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def show_info(self):
        print(f'单位状态，生命值{self.hp}')

    ###
    def attack(self, target):
        damage = self.power + random.randint(-10, 10)
        target.hp -= damage
        print(f'受到{damage}点伤害')

        if target.hp <= 0:
            return True

###
class Hero(Unit):

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        self.name = name

    def show_info(self):
        print(f'英雄{self.name}状态，生命值{self.hp}')

###
hero_name = input('请输入英雄的名字：')

###
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

hero.show_info()
enemy.show_info()

while True:
    if hero.attack(enemy):
        print('英雄胜利')
        break
    else:
        enemy.show_info()

    if enemy.attack(hero):
        print('英雄阵亡')
        break
    else:
        hero.show_info()
