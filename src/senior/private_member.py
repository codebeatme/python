
###
class Unit:

    def __init__(self, hp, power):
        self.__hp = hp
        self.power = power

    def __hurt():
        pass

###
class Hero(Unit):

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        self.name = name

        print(f'{self.name}状态 攻击力{self.power}')

###
hero = Hero(100, 10, '钢铁侠')
# hero.__hp += 100