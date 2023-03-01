# 视频内容：「Python」进阶教程 如何读取写入文件？如何打开关闭文件
# 视频地址：https://www.bilibili.com/video/BV1GM4y1o7Qi/

###
class Student:

    def __init__(self, n, a):
        self.name = n
        self.age = a

###
students = []

file = open('D:/student.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    if line:
        args = line.split(' ')
        name = args[0]
        age = int(args[1])

        students.append(Student(name, age))
        
while True:
    text = input('请输入姓名和年龄，使用空格分割：')

    if text == 'n':
        break

    ###
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])

    student = Student(input_name, input_age)

    students.append(student)

###
lines = []

for s in students:
    lines.append(f'{s.name} {s.age}\n')
    print(f'学生{s.name} 年龄{s.age}')

file = open('D:/student.txt', 'w')
file.writelines(lines)
file.close()
