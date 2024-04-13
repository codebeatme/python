class A:
    name = 'A'
    def show(self):
        print('调用 A 的 show 方法')

class B1(A):
    pass

class B2(A):
    def show(self):
        print('调用 B2 的 show 方法')
    

class C(B1, B2):
    pass

# 不会产生多义性问题，因为类 A 仅被搜索一次
print(C.name)
c = C()
# 调用 B2 的 show 方法，而不是 A 的 show 方法
c.show()