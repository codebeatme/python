class A:
    name = 'A'
    def show(self):
        print('Call the show method of A')

class B1(A):
    pass

class B2(A):
    def show(self):
        print('Call the show method of B2')
    

class C(B1, B2):
    pass

# There is no ambiguity problem because class A is only searched once
print(C.name)
c = C()
# This calls B2's show method instead of A's show method
c.show()