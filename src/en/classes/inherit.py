# A class on people
class Person:
    title = 'How to address?'

    def __init__(self, name, age):
        # Define class instance variables name, age
        self.name = name
        self.age = age

# A class that represents a good person, inherited from Person
class GoodMan(Person):
    pass

# Create an instance of GoodMan
goodman = GoodMan('Good man', 40)

# Determine whether the instance goodman is Person or int
print(isinstance(goodman, (Person, int)))
# Determine whether the instance goodman is one of int, float, or str
print(isinstance(goodman, int | float | str))

# Determine if class GoodMan is a subclass of object
print(issubclass(GoodMan, object))
# Determine if class GoodMan is a subclass of str or Person
print(issubclass(GoodMan, str | Person))
# Determine if class GoodMan is a subclass of GoodMan
print(issubclass(GoodMan, GoodMan))