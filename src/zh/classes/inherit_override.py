# 一个游戏单位
class Unit:
    # 用于发起攻击的方法
    def attack(self):
        print('Unit 发起攻击')

class Hero(Unit):
    # 该方法将被之后定义的 attack 覆盖
    def attack(self, times):
        while times > 0:
            print('Hero 发起攻击')
            times -= 1

    # 将重写 Unit 的 attack 方法，并覆盖之前定义的 attack
    def attack(self, times):
        print(f'Hero 将发起 {times} 次攻击')

Unit().attack()
Hero().attack(5)
# ERROR 无法调用 Unit 类定义的 attack 方法
Hero().attack()