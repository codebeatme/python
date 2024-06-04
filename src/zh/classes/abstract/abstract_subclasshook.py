from abc import ABC

class Unit(ABC):
    # 所有的类都不是 Unit 的派生类
    @classmethod
    def __subclasshook__(cls, subclass):
        print(f'{subclass} 是 Unit 的派生类吗？')
        return False

class Player(Unit):
    pass

# 查看 Player 与 Unit 之间的关系
print(issubclass(Player, Unit))
print(isinstance(Player(), Unit))