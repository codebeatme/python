from abc import ABCMeta

# Abstract base class representing movable
class Movable(metaclass=ABCMeta):
    pass

# Show Movable's Method Resolution Order and base classes
print(Movable.__mro__)
print(Movable.__bases__)

from abc import ABC

# Abstract base class representing accessible
class Accessible(ABC):
    pass

# Show Accessible's Method Resolution Order and base classes
print(Accessible.__mro__)
print(Accessible.__bases__)
