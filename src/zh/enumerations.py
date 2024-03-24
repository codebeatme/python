import enum

class A(enum.Enum):
    pass

class B(enum.Enum):
    Name = 1

class C:
    JACK = 2
    pass

class D:
    pass

print(type(A) is type(B))
print(type(C()))
print(type(D()))
print(type(enum.Enum('Color', ['RED', 'GREEN', 'BLUE'])))