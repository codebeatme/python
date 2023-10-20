'''
本节文章
https://learnscript.net/zh/python/advanced/implementing-method-overriding/ 如何实现方法重写
'''

###
class Unit:
    # 类 Unit，表示游戏中的单位

    def __init__(self, hp, power):
        # 表示生命值和力量值的字段
        self.hp = hp
        self.power = power

    def show_status(self):
        # 显示单位的相关状态
        print(f'单位状态，生命值 {self.hp}，力量值 {self.power}')

###
class Hero(Unit):
    # 类 Hero，表示玩家控制的英雄

    def __init__(self, hp, power, name):
        super().__init__(hp, power)
        # 表示英雄名字的字段 name
        self.name = name

    def show_status(self):
        # 重写 Unit 类的 show_status 方法
        # 通过 super() 调用 Unit 的 show_status，显示生命值和力量值
        super().show_status()
        print(f'英雄名 {self.name}')

###
hero_name = input('请输入英雄的名字：')

### 分别创建 Hero 类和 Unit 类的实例
hero = Hero(100, 10, hero_name)
enemy = Unit(100, 10)

### hero，enemy 将以不同的方式来显示状态
print('hero 显示状态')
hero.show_status()
print('enemy 显示状态')
enemy.show_status()
