# 视频内容：「Python」高级教程 如何定义和调用类的静态方法？staticmethod与classmethod的区别
# 视频地址：https://www.bilibili.com/video/BV1kM4y1k7fg/

###
class Unit:
    count = 0

    ###
    @staticmethod
    def random_id():
        import random
        return f'id_{random.randint(1,10000000)}'

    ###
    @classmethod
    def show_board(cls):
        print(f'总计{cls.count}个单位')

    ###
    def __init__(self, hp):
        self.id = Unit.random_id()
        self.hp = hp
        Unit.count += 1

###
u1 = Unit(100)
print(f'u1.id={u1.id}')
u1.show_board()