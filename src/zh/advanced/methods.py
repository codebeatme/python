'''
本节文章
https://learnscript.net/zh/python/advanced/define-and-call-class-methods/ 如何定义和调用类的方法
'''

###


class Student:
    # 类 Student，表示一个学生

    def __init__(self):
        # 定义字段表示学生的姓名，年龄，分数，并设置默认值
        self.name = '无名氏'
        self.age = 0
        self.scores = []

    def sum_score(self):
        # 方法 sum_score，用来计算总分数
        total = 0

        # 将字段 scores 包含的所有分数相加
        for score in self.scores:
            total += int(score)

        return total


###
students = []

while True:
    # 要求输入学生的相关信息
    text = input('请输入姓名和年龄以及分数，使用空格分割：')

    # n 表示结束输入
    if text == 'n':
        break

    ### 使用输入的学生信息，创建 Student 类的实例，并保存到列表
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])
    input_scores = args[2:]

    student = Student()
    # 依次设置字段
    student.name = input_name
    student.age = input_age
    student.scores = input_scores

    students.append(student)

###
for s in students:
    # 调用方法 sum_score，获取该学生的总分数
    total_score = s.sum_score()
    print(f'学生：{s.name} 年龄：{s.age} 总分数：{total_score}')
