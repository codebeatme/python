from abc import ABCMeta

# 表示可移动的抽象基类
class Movable(metaclass=ABCMeta):
    pass

# 显示 Movable 的方法解析顺序和基类
print(Movable.__mro__)
print(Movable.__bases__)

from abc import ABC

# 表示可访问的抽象基类
class Accessible(ABC):
    pass

# 显示 Accessible 的方法解析顺序和基类
print(Accessible.__mro__)
print(Accessible.__bases__)
