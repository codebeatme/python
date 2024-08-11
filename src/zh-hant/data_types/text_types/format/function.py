# 一個用於格式化的類別
class Data:
    def __format__(self, format_spec):
        return '__format__'
    def __str__(self):
        return '__str__'
    def __repr__(self):
        return '<物件 "Data">'

# 物件的 __format__ 方法將被呼叫
print('{}'.format(Data()))
# str 的建構子將被呼叫
print('{!s}'.format(Data()))
# repr 函式將被呼叫
print('{!r}'.format(Data()))
# ascii 函式將被呼叫
print('{0!a}'.format(Data()))
