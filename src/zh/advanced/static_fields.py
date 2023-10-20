'''
本节文章
https://learnscript.net/zh/python/advanced/define-and-access-class-static-fields/ 如何定义和访问类的静态字段
'''

###
import random


class Unit:
    # 类 Unit，表示游戏中的单位

    # 静态字段 count，表示存活单位的个数
    count = 0

    def __init__(self, hp):
        # 设置单位的初始状态，包括生命值，死亡状态
        self.hp = hp
        self.dead = False
        # 存活单位的个数加 1
        Unit.count += 1

    ###
    def hurt(self, damage):
        # 让单位受伤的方法

        # 根据伤害扣除生命值
        self.hp -= damage
        print(f'一个单位受到 {damage} 点伤害')

        # 生命值小于等于 0，则认为单位死亡，存活单位的个数减 1
        if self.hp <= 0:
            self.dead = True
            Unit.count -= 1
            print(f'一个单位死亡，剩余 {Unit.count} 个单位')


### 创建三个游戏单位，状态为存活
units = [Unit(10), Unit(15), Unit(20)]
game_over = False

while not game_over:

    # 依次让所有存活单位受到伤害，直到仅剩一个存活单位时
    for unit in units:
        if not unit.dead:
            # 伤害大小是随机的
            damage = random.randint(0, 10)
            unit.hurt(damage)

            # 仅剩一个存活单位，则跳出循环，游戏结束
            if Unit.count == 1:
                game_over = True
                break

print('游戏结束')

# 定义静态字段 type_name，表示 Unit 的类别名称
Unit.type_name = '单位'
print(f'Unit 的类别名称为：{Unit.type_name}')
