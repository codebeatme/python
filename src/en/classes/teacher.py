# A class representing a teacher
class Teacher:
    # Constructor
    def __init__(self, n, a):
        # Private instance variables __name, __age
        self.__name = n
        self.__age = a

teacher = Teacher('Invisible Man', 30)
# Show all the attributes of the Teacher instance
print(teacher.__dict__)
# Access the private variable __name in a special way
print(teacher._Teacher__name)