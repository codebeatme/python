from abc import ABCMeta, abstractmethod

class Plant(metaclass=ABCMeta):
    # 定義抽象方法 grow
    @abstractmethod
    def grow(self):
        print('Plant 生長吧！')

class Flower(Plant):
    # 覆寫抽象方法 grow，以實作他
    def grow(self):
        super().grow()
    
    # 定義抽象類別方法 count
    @classmethod
    @abstractmethod
    def count(self):
        pass

class BigFlower(Flower):
    # 覆寫抽象類別方法 count，以實作他
    @classmethod
    def count(self):
        print('一共有多少個哪？')

# 不能建立 Plant 和 Flower 的執行個體
BigFlower().grow()