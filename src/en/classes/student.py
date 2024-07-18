# A class representing a student
class Student:
    # Class variable count
    count = 0
    # Constructor
    def __init__(self, n, a):
        # Instance variables name, age
        self.name = n
        self.age = a

    # Instance method info
    def info(self):
        print(f'{self.name} {self.age}')

    # Class method show
    @classmethod
    def show(cls):
        # Read the class variable count via the parameter cls
        print(f'{cls.count} student(s) in total')
        
    # Static method set_count
    @staticmethod
    def set_count(c):
        # The class variable count can only be accessed through the class
        Student.count = c
        print(f'The number of students is set to {Student.count}')

student = Student('Jack', 13)
# Call the instance method info
student.info()
Student.info(student)
# Call the static method set_count
student.set_count(-100)
Student.set_count(100)
# Call the class method show
student.show()
Student.show()

# Get the type information of the Student class and the previously created instance student
print(student.__class__)
print(Student.__class__)