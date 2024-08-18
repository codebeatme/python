from abc import ABC

class Unit(ABC):
    # None of the classes are derived from the Unit
    @classmethod
    def __subclasshook__(cls, subclass):
        print(f'Is {subclass} a derived class of Unit?')
        return False

class Player(Unit):
    pass

# View the relationship between Player and Unit
print(issubclass(Player, Unit))
print(isinstance(Player(), Unit))