  # 一个关于人的类
class Person:
    title = '该如何称呼哪？'

    def __init__(self, name, age):
        # 定义类的实例变量 name，age
        self.name = name
        self.age = age

# 表示好人的类，从 Person 继承
class GoodMan(Person):
    pass

# 创建 GoodMan 的实例
goodman = GoodMan('好心人', 40)

# 判断实例 goodman 的类型是否为 Person 或 int
print(isinstance(goodman, (Person, int)))
# 判断实例 goodman 的类型是否为 int，float，str 中的一个
print(isinstance(goodman, int | float | str))

# 判断类 GoodMan 是否为 object 的子类
print(issubclass(GoodMan, object))
# 判断类 GoodMan 是否为 str 或 Person 的子类
print(issubclass(GoodMan, str | Person))
# 判断类 GoodMan 是否为 GoodMan 的子类
print(issubclass(GoodMan, GoodMan))