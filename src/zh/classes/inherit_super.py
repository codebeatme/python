class Animal:
    @staticmethod
    def show():
        print('这里是 Animal！')

    @classmethod
    def eat(cls, something):
        print(f'Animal 吃点 {something}')

    def run(self):
        print('Animal 奔跑起来了！')

class Cat(Animal):
    @staticmethod
    def show():
        print('Cat 调用 Animal 的静态方法 show')
        super(Cat, Cat).show()

    @classmethod
    def eat(cls, something):
        print('Cat 调用 Animal 的类方法 eat')
        super().eat(something)

    def run(self):
        print('Cat 调用 Animal 的实例方法 run')
        # 相当于 super(Cat, self).run()
        super().run()

class Dog(Animal):
    def run(self):
        print('Dog 奔跑起来了！')

class BigDog(Dog):
    def run(self):
        print('BigDog 调用 Animal 的 run 方法')
        super(Dog, self).run()

Cat.show()
Cat.eat('小鱼干')
Cat().run()
dog = BigDog()
dog.run()
# 调用 Dog 中的 run 方法
super(BigDog, dog).run()
