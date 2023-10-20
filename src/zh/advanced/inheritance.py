'''
本节文章
https://learnscript.net/zh/python/advanced/implementing-class-inheritance/ 如何实现类的继承
'''

###
class Unit:
    # 类 Unit，表示游戏中的单位

    def __init__(self, hp, power):
        # 表示生命值和力量值的字段
        self.hp = hp
        self.power = power

###
class Hero(Unit):
    # 类 Hero，继承自 Unit，表示玩家控制的英雄

    def __init__(self, hp, power, name):
        # 通过 super() 来访问基类 Unit 的构造方法
        super().__init__(hp, power)
        # 对比 Unit 类，增加一个表示名字的字段 name
        self.name = name

###
hero_name = input('请输入英雄的名字：')

### 分别创建 Hero 类和 Unit 类的实例
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

print(f'玩家状态，英雄 {hero.name}，生命值 {hero.hp}，力量值 {hero.power}')
print(f'敌人状态，生命值 {enemy.hp}，力量值 {enemy.power}')
