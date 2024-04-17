from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    # 抽象類別方法 count
    @classmethod
    @abstractmethod
    def count(cls):
        pass

    # 抽象靜態方法 name
    @staticmethod
    @abstractmethod
    def name():
        print('名字到底是什麽啊？')

class Cat(Animal):
    pass

# 呼叫未實作的靜態方法 name 和類別方法 count
Cat.name()
Animal.count()
# ERROR Cat 並未實作抽象基底類別 Animal
Cat().name()