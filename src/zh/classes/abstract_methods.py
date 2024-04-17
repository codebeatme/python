from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    # 抽象类方法 count
    @classmethod
    @abstractmethod
    def count(cls):
        pass

    # 抽象静态方法 name
    @staticmethod
    @abstractmethod
    def name():
        print('名字到底是什么啊？')

class Cat(Animal):
    pass

# 调用未实现的静态方法 name 和类方法 count
Cat.name()
Animal.count()
# ERROR Cat 并未实现抽象基类 Animal
Cat().name()