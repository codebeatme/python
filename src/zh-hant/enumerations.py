from enum import *
from typing import Any


class SPORT(Enum):
    '''一個關於運動的列舉，包含了籃球，足球和棒球'''
    FOOTBALL = 1
    BASKETBALL = 2
    BASEBALL = 3
    SOCCER = 1


# 定義列舉 PLANT
PLANT = StrEnum('PLANT', (['TREE', 'one tree'], ['FLOWER', 'one flower']))
print(PLANT.__members__)


print(type(SPORT.FOOTBALL))
# 判斷成員 FOOTBALL 是否為 SPORT 的執行個體
print(isinstance(SPORT.FOOTBALL, SPORT))
    
# 列舉成員 A 和 B 將出現在模組中
@global_enum
class LETTER(Enum):
    A = 'a'
    B = 'b'

# 下面的存取方式都是正確的
print(LETTER.A)
print(A)

# 列舉 NUM 的成員的值需要是連貫的
@verify(CONTINUOUS)
class NUM(Enum):
    ONE = 1
    TWO = 2
    FOUR = 4
    THREE = 3

class POSITION(Enum):
    _ignore_ = ('Z', 'W')
    # X 不是列舉成員
    X = nonmember(1)
    # Y 是列舉成員
    Y = 2
    # Z 和 W 不是列舉成員，雖然 W 使用了 member
    Z = 3
    W = member(4)

print(POSITION.__members__)

print(SPORT.SOCCER)
print(SPORT.SOCCER.name)

# 這裏不會出現 SOCCER，因為他是 FOOTBALL 的別名
for i in SPORT:
    print(f'{i.name}={i.value}')


# 可以將 @verify(UNIQUE) 取代為 @unique
@verify(UNIQUE)
class ROLE(Enum):
    PLAYER = 1
    # ERROR 這裏不能出現別名
    # HERO = 1


# 顯示 SPORT 的全部成員，包括 SOCCER
print(SPORT.__members__)

print(SPORT.FOOTBALL == SPORT.SOCCER)
print(SPORT.FOOTBALL != 1)

# 取得列舉 NUM 中已經定義的成員的個數
print(f'NUM 成員的個數為：{len(NUM)}')

football = SPORT.FOOTBALL

# 重新定義列舉 SPORT


class SPORT(Enum):
    FOOTBALL = 1
    BASKETBALL = 2
    BASEBALL = 3
    SOCCER = 1


# 比較之前和新的列舉成員 FOOTBALL，傳回 False
print(football == SPORT.FOOTBALL)


class DIRECTION(Enum):
    # 需要定義在所有列舉成員之前
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f'{name}_{count}'

    UP = auto()
    RIGHT = auto()
    DOWN = 100
    # 將根據 100 傳回 101
    LEFT = auto()


print(f'{DIRECTION.UP.value} {DIRECTION.RIGHT.value} {DIRECTION.DOWN.value} {DIRECTION.LEFT.value}')

class DAY(str, ReprEnum):
    MONDAY = 1
    TUESDAY = 2

    # self 代表了列舉成員
    def show(self):
        print(f'{self.name}={self.value}')

DAY.TUESDAY.show()

class SPEED(int, Enum):
    def __new__(cls, *args):
        # 計算所有數值的和，並儲存至 total
        total = 0
        for i in args:
            total += i

        # 建立列舉的執行個體，並將之前的計算結果指派給 _value_
        prop = int.__new__(cls)
        prop._value_ = total
        return prop

    LOW = (1, 2, 3, 4, 5)
    HIGH = (6, 7, 8, 9)

print(SPEED.LOW.value)


class ANIMAL(Enum):
    DOG = 100
    CAT = 200

    # 處理超出取值範圍的列舉成員
    @classmethod
    def _missing_(cls, value):
        if type(value) is int:
            if value < 100:
                # 小於 100 的整數，將被認為是 DOG
                return ANIMAL.DOG
            elif value < 200:
                # 大於 100 小於 200 的整數，將被認為是 CAT
                return ANIMAL.CAT
            
        # 其余取值傳回 None，這將導致例外狀況的發生
        return None

print(ANIMAL(99))
print(ANIMAL(111))

class JOB(IntEnum):
    WORKER = 1
    DOCTOR = '100', 8

# 參與算術運算後，運算結果不再是某個列舉成員
print(f'{type(JOB.WORKER)} {type(JOB.DOCTOR)}')
print(type(JOB.WORKER + 3))
print(type(JOB.WORKER + JOB.DOCTOR))

class HERO(str, ReprEnum):
    # 123 會被轉換為 '123'
    TOM = 123
    JERRY = 'mouse?'

class TIME(StrEnum):
    SECOND = 'sec'
    # ERROR 1 並不會轉換為 '1'
    # MINUTE = 1

# class AAA(Enum):
#     # def a(self):
#     #     pass
#     # _ignore_ = ('a', 'W')
#     ABC = auto()
#     # 需要定義在所有列舉成員之前
#     @staticmethod
#     def _generate_next_value_(name, start, count, last_values):
#         return f'{name}_{count}'
#     ABC2 = auto()


# # AAA.a > 0