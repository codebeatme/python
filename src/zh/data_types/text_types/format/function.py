# 一个用于格式化的类
class Data:
    def __format__(self, format_spec):
        return '__format__'
    def __str__(self):
        return '__str__'
    def __repr__(self):
        return '<对象 "Data">'

# 对象的 __format__ 方法将被调用
print('{}'.format(Data()))
# str 的构造器将被调用
print('{!s}'.format(Data()))
# repr 函数将被调用
print('{!r}'.format(Data()))
# ascii 函数将被调用
print('{0!a}'.format(Data()))
