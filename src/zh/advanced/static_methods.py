'''
本节文章
https://learnscript.net/zh/python/advanced/define-and-call-class-static-methods/ 如何定义和调用类的静态方法
'''

###


class Unit:
    # 类 Unit，表示游戏单位

    # 静态字段，表示单位数量
    count = 0

    ###
    @staticmethod
    def random_id():
        # 静态方法 random_id，用于生成一个随机 id
        import random
        num = random.randint(1, 10000000)
        return f'id_{num}'

    ###
    @classmethod
    def show_info(cls):
        # 静态方法 show_info，用来显示一些信息
        print(f'总计 {cls.count} 个单位')

    ###
    def __init__(self, hp):
        # 生成一个随机 id，并保存在 id 字段中
        self.id = self.random_id()
        self.hp = hp
        Unit.count += 1


###
# 创建 Unit 类的实例
unit = Unit(100)
print(f'unit.id={unit.id}')
# 通过类调用静态方法
Unit.show_info()
