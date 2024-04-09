class Teacher1:
    # 類別 Teacher，表示了教師

    def __init__(self, n, a):
        # 建構方法，使用參數 n，a，初始化欄位 name，age
        self.name = n
        self.age = a
        self.abc = lambda x,y:x+y

    def give(self):
        pass

    def __give(self, a):
        print(a)

    _GG = 11

    class A:
        pass

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.deleter
    def x(self):
        del self._x

    def x1(self, value):
        self._x = value

class Teacher2(Teacher):
    def give2(self, a):
        return super().give()

print(Teacher(0,0).__dict__)
print(Teacher.__dict__)

Teacher(0,0)._Teacher__give(2)
Teacher2(0,0).give2(1)

Teacher.x1()