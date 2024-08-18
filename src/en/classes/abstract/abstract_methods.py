from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    # Abstract class method count
    @classmethod
    @abstractmethod
    def count(cls):
        pass

    # Abstract static method name
    @staticmethod
    @abstractmethod
    def name():
        print('What\'s the name?')

class Cat(Animal):
    pass

# Calls the unimplemented static method name and the unimplemented class method count
Cat.name()
Animal.count()
# ERROR Cat does not implement the abstract base class Animal
Cat().name()