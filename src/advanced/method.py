class Student:

    def __init__(self, n, a):
        self.name = n
        self.age = a

students = []

while True:
    text = input('请输入姓名和年龄，使用空格分割：')

    if text == 'n':
        break

    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])

    student = Student(input_name, input_age)

    students.append(student)

for s in students:
    print(f'学生{s.name} 年龄{s.age}')