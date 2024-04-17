from abc import ABCMeta, abstractmethod

class Plant(metaclass=ABCMeta):
    # 定义抽象方法 grow
    @abstractmethod
    def grow(self):
        print('Plant 生长吧！')

class Flower(Plant):
    # 重写抽象方法 grow，以实现他
    def grow(self):
        super().grow()
    
    # 定义抽象类方法 count
    @classmethod
    @abstractmethod
    def count(self):
        pass

class BigFlower(Flower):
    # 重写抽象类方法 count，以实现他
    @classmethod
    def count(self):
        print('一共有多少个哪？')

# 不能创建 Plant 和 Flower 的实例
BigFlower().grow()