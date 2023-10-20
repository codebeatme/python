'''
本节文章
https://learnscript.net/zh/python/advanced/generate-random-numbers/ 如何生成随机数
'''

### 导入 random 模块
import random

# 使用 randint 获取随机整数
num1 = random.randint(0, 10)
# 使用 random 获取随机浮点数
num2 = random.random()

print(f'随机整数：{num1}')
print(f'随机浮点数：{num2}')

class Unit:
    # 类 Unit，表示游戏中的单位

    def __init__(self, hp, power):
        # 表示生命值和力量值的字段
        self.hp = hp
        self.power = power

    def show_status(self):
        # 显示单位的相关状态
        print(f'单位状态，生命值 {self.hp}')

    def attack(self, target):
        # 方法 attack 用来攻击另一个游戏单位

        # 通过 randint 生成一个随机的伤害值
        damage = self.power + random.randint(-10, 10)

        # 根据伤害值减少生命值，小于等于 0 返回 True，表示单位被击败
        target.hp -= damage
        print(f'受到 {damage} 点伤害')

        if target.hp <= 0:
            return True

###
class Hero(Unit):
    # 类 Hero，表示玩家控制的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的字段 name
        self.name = name

    def show_status(self):
        # 显示英雄的相关状态
        print(f'英雄名 {self.name}，生命值 {self.hp}')

###
hero_name = input('请输入英雄的名字：')

### 分别创建 Hero 类和 Unit 类的实例
hero = Hero(40, 10, hero_name)
enemy = Unit(40, 10)

# 显示英雄和敌人的初始状态
hero.show_status()
enemy.show_status()

# 让英雄和敌人相互攻击，直到其中一方死亡
while True:
    # 英雄首先攻击敌人
    if hero.attack(enemy):
        print('英雄胜利')
        break
    else:
        # 如果敌人还活着，则显示他的状态
        enemy.show_status()

    # 敌人攻击英雄
    if enemy.attack(hero):
        print('英雄阵亡')
        break
    else:
        # 如果英雄还活着，则显示他的状态
        hero.show_status()
