class Animal:
    @staticmethod
    def show():
        print('這裏是 Animal！')

    @classmethod
    def eat(cls, something):
        print(f'Animal 吃點 {something}')

    def run(self):
        print('Animal 奔跑起來了！')

class Cat(Animal):
    @staticmethod
    def show():
        print('Cat 呼叫 Animal 的靜態方法 show')
        super(Cat, Cat).show()

    @classmethod
    def eat(cls, something):
        print('Cat 呼叫 Animal 的類別方法 eat')
        super().eat(something)

    def run(self):
        print('Cat 呼叫 Animal 的執行個體方法 run')
        # 相當於 super(Cat, self).run()
        super().run()

class Dog(Animal):
    def run(self):
        print('Dog 奔跑起來了！')

class BigDog(Dog):
    def run(self):
        print('BigDog 呼叫 Animal 的 run 方法')
        super(Dog, self).run()

Cat.show()
Cat.eat('小魚幹')
Cat().run()
dog = BigDog()
dog.run()
# 呼叫 Dog 中的 run 方法
super(BigDog, dog).run()
