from abc import ABCMeta, abstractmethod

class Plant(metaclass=ABCMeta):
    # Define the abstract method grow
    @abstractmethod
    def grow(self):
        print('Plant: Grow it!')

class Flower(Plant):
    # Override the abstract method grow to implement it
    def grow(self):
        super().grow()
    
    # Define the abstract class method count
    @classmethod
    @abstractmethod
    def count(self):
        pass

class BigFlower(Flower):
    # Override the abstract method count to implement it
    @classmethod
    def count(self):
        print('How many are there?')

# Cannot create instances of Plant and Flower
BigFlower().grow()