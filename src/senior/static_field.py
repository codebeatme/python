###
class Unit:
    count = 0

    def __init__(self, hp):
        self.hp = hp
        self.dead = False
        Unit.count += 1

    ###
    def hurt(self, damage):
        self.hp -= damage
        print(f'一个单位受到{damage}点伤害')

        if self.hp <= 0:
            self.dead = True
            Unit.count -= 1
            print(f'一个单位死亡，剩余{Unit.count}个单位')

###
import random
units = [Unit(10), Unit(15), Unit(20)]
game_over = False

while not game_over:

    for unit in units:
        if not unit.dead:
            damage = random.randint(0, 10)
            unit.hurt(damage)

            if Unit.count == 1:
                game_over = True
                break

print('游戏结束')