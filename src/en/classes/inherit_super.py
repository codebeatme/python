class Animal:
    @staticmethod
    def show():
        print('Here\'s Animal!')

    @classmethod
    def eat(cls, something):
        print(f'Animal: Eat some {something}')

    def run(self):
        print('Animal: Let\'s run!')

class Cat(Animal):
    @staticmethod
    def show():
        print('Cat calls Animal\'s static method show')
        super(Cat, Cat).show()

    @classmethod
    def eat(cls, something):
        print('Cat calls Animal\'s class method eat')
        super().eat(something)

    def run(self):
        print('Cat calls Animal\'s instance method run')
        # Equivalent to super(Cat, self).run()
        super().run()

class Dog(Animal):
    def run(self):
        print('Dog: Let\'s run!')

class BigDog(Dog):
    def run(self):
        print('BigDog calls Animal\'s method run')
        super(Dog, self).run()

Cat.show()
Cat.eat('Small dried fish')
Cat().run()
dog = BigDog()
dog.run()
# Call the run method in Dog
super(BigDog, dog).run()
