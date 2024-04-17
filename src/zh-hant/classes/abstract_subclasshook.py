from abc import ABC

class Unit(ABC):
    # 所有的類別都不是 Unit 的衍生類別
    @classmethod
    def __subclasshook__(cls, subclass):
        print(f'{subclass} 是 Unit 的衍生類別嗎？')
        return False

class Player(Unit):
    pass

# 檢視 Player 與 Unit 之間的關系
print(issubclass(Player, Unit))
print(isinstance(Player(), Unit))