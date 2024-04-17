from abc import ABCMeta

# 表示可移動的抽象基底類別
class Movable(metaclass=ABCMeta):
    pass

# 顯示 Movable 的方法解析順序和基底類別
print(Movable.__mro__)
print(Movable.__bases__)

from abc import ABC

# 表示可存取的抽象基底類別
class Accessible(ABC):
    pass

# 顯示 Accessible 的方法解析順序和基底類別
print(Accessible.__mro__)
print(Accessible.__bases__)
