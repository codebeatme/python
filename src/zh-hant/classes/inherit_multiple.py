class A:
    name = 'A'
    def show(self):
        print('呼叫 A 的 show 方法')

class B1(A):
    pass

class B2(A):
    def show(self):
        print('呼叫 B2 的 show 方法')
    

class C(B1, B2):
    pass

# 不會產生語意模糊問題，因為類別 A 僅被搜尋一次
print(C.name)
c = C()
# 呼叫 B2 的 show 方法，而不是 A 的 show 方法
c.show()