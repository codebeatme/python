'''
使用类或实例访问静态字段有何异同
* 实例仅能读取静态字段，而类即可以读取也可以修改
* 如果通过实例修改静态字段，则只会对其自身有效果

版本
Python 3.11.1
VSCode 1.76.0

关于本系列教程的使用说明和相关问题解答，请参考文章 https://www.bilibili.com/read/cv23030766
'''

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

