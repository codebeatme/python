from enum import *
from typing import Any


class SPORT(Enum):
    '''一个关于运动的枚举，包含了篮球，足球和棒球'''
    FOOTBALL = 1
    BASKETBALL = 2
    BASEBALL = 3
    SOCCER = 1


# 定义枚举 PLANT
PLANT = StrEnum('PLANT', (['TREE', 'one tree'], ['FLOWER', 'one flower']))
print(PLANT.__members__)


print(type(SPORT.FOOTBALL))
# 判断成员 FOOTBALL 是否为 SPORT 的实例
print(isinstance(SPORT.FOOTBALL, SPORT))
    
# 枚举成员 A 和 B 将出现在模块中
@global_enum
class LETTER(Enum):
    A = 'a'
    B = 'b'

# 下面的访问方式都是正确的
print(LETTER.A)
print(A)

# 枚举 NUM 的成员的值需要是连贯的
@verify(CONTINUOUS)
class NUM(Enum):
    ONE = 1
    TWO = 2
    FOUR = 4
    THREE = 3

class POSITION(Enum):
    _ignore_ = ('Z', 'W')
    # X 不是枚举成员
    X = nonmember(1)
    # Y 是枚举成员
    Y = 2
    # Z 和 W 不是枚举成员，虽然 W 使用了 member
    Z = 3
    W = member(4)

print(POSITION.__members__)

print(SPORT.SOCCER)
print(SPORT.SOCCER.name)

# 这里不会出现 SOCCER，因为他是 FOOTBALL 的别名
for i in SPORT:
    print(f'{i.name}={i.value}')


# 可以将 @verify(UNIQUE) 替换为 @unique
@verify(UNIQUE)
class ROLE(Enum):
    PLAYER = 1
    # ERROR 这里不能出现别名
    # HERO = 1


# 显示 SPORT 的全部成员，包括 SOCCER
print(SPORT.__members__)

print(SPORT.FOOTBALL == SPORT.SOCCER)
print(SPORT.FOOTBALL != 1)

# 获取枚举 NUM 中已经定义的成员的个数
print(f'NUM 成员的个数为：{len(NUM)}')

football = SPORT.FOOTBALL

# 重新定义枚举 SPORT


class SPORT(Enum):
    FOOTBALL = 1
    BASKETBALL = 2
    BASEBALL = 3
    SOCCER = 1


# 比较之前和新的枚举成员 FOOTBALL，返回 False
print(football == SPORT.FOOTBALL)


class DIRECTION(Enum):
    # 需要定义在所有枚举成员之前
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f'{name}_{count}'

    UP = auto()
    RIGHT = auto()
    DOWN = 100
    # 将根据 100 返回 101
    LEFT = auto()


print(f'{DIRECTION.UP.value} {DIRECTION.RIGHT.value} {DIRECTION.DOWN.value} {DIRECTION.LEFT.value}')

class DAY(str, ReprEnum):
    MONDAY = 1
    TUESDAY = 2

    # self 代表了枚举成员
    def show(self):
        print(f'{self.name}={self.value}')

DAY.TUESDAY.show()

class SPEED(int, Enum):
    def __new__(cls, *args):
        # 计算所有数字的和，并保存至 total
        total = 0
        for i in args:
            total += i

        # 创建枚举的实例，并将之前的计算结果赋值给 _value_
        prop = int.__new__(cls)
        prop._value_ = total
        return prop

    LOW = (1, 2, 3, 4, 5)
    HIGH = (6, 7, 8, 9)

print(SPEED.LOW.value)


class ANIMAL(Enum):
    DOG = 100
    CAT = 200

    # 处理超出取值范围的枚举成员
    @classmethod
    def _missing_(cls, value):
        if type(value) is int:
            if value < 100:
                # 小于 100 的整数，将被认为是 DOG
                return ANIMAL.DOG
            elif value < 200:
                # 大于 100 小于 200 的整数，将被认为是 CAT
                return ANIMAL.CAT
            
        # 其余取值返回 None，这将导致异常的发生
        return None

print(ANIMAL(99))
print(ANIMAL(111))

class JOB(IntEnum):
    WORKER = 1
    DOCTOR = '100', 8

# 参与算术运算后，运算结果不再是某个枚举成员
print(f'{type(JOB.WORKER)} {type(JOB.DOCTOR)}')
print(type(JOB.WORKER + 3))
print(type(JOB.WORKER + JOB.DOCTOR))

class HERO(str, ReprEnum):
    # 123 会被转换为 '123'
    TOM = 123
    JERRY = 'mouse?'

class TIME(StrEnum):
    SECOND = 'sec'
    # ERROR 1 并不会转换为 '1'
    # MINUTE = 1

# class AAA(Enum):
#     # def a(self):
#     #     pass
#     # _ignore_ = ('a', 'W')
#     ABC = auto()
#     # 需要定义在所有枚举成员之前
#     @staticmethod
#     def _generate_next_value_(name, start, count, last_values):
#         return f'{name}_{count}'
#     ABC2 = auto()


# # AAA.a > 0