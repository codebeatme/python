# 视频内容：「Python」高级教程 类和实例访问静态字段的区别是什么？实例修改静态字段陷阱
# 视频地址：https://www.bilibili.com/video/BV1YM41147Hw/

###
class Unit:
    count = 0

    def __init__(self, hp):
        self.hp = hp
        self.dead = False
        Unit.count += 1

###
u1 = Unit(10)
u2 = Unit(10)
print(f'u1.count={u1.count}')
print(f'u2.count={u2.count}')
print(f'Unit.count={Unit.count}')

u1.count = 0
u3 = Unit(10)
print(f'u1.count={u1.count}')
print(f'u2.count={u2.count}')
print(f'u3.count={u3.count}')
print(f'Unit.count={Unit.count}')

