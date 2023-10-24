'''
本节文章
https://learnscript.net/zh/python/advanced/reading-and-writing-files/ 如何读取和写入文件
'''

###


class Student:
    # 类 Student，表示一个学生

    def __init__(self, n, a):
        # 定义字段表示学生的姓名，年龄
        self.name = n
        self.age = a


# 从文件 student.txt 读取学生信息
students = []

file = open('student.txt', 'r')
lines = file.readlines()
file.close()

# 将从文件读取的每一行转换为学生对象
for line in lines:
    # 忽略空行
    if line:
        args = line.split(' ')
        name = args[0]
        age = int(args[1])

        students.append(Student(name, age))

while True:
    # 要求输入学生的相关信息
    text = input('请输入姓名和年龄，使用空格分割：')

    # n 表示结束输入
    if text == 'n':
        break

    # 使用输入的学生信息，创建 Student 类的实例，并保存到列表
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])

    student = Student(input_name, input_age)

    students.append(student)

# 将学生信息转换为字符串，并保存到列表 lines
lines = []

for s in students:
    lines.append(f'{s.name} {s.age}\n')
    print(f'学生{s.name} 年龄 {s.age}')

# 将列表 lines 写入到文件 student.txt
file = open('student.txt', 'w')
file.writelines(lines)
file.close()
