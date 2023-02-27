###
class Unit:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

###
class Hero(Unit):

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        self.name = name

###
hero_name = input('请输入英雄的名字：')

###
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

print(f'玩家状态，英雄{hero.name}，生命值{hero.hp}，攻击力{hero.power}')
print(f'敌人状态，生命值{enemy.hp}，攻击力{enemy.power}')