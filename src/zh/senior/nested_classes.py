'''
本节文章
https://learnscript.net/zh/python/senior/define-nested-classes/ 如何定义和使用嵌套类
'''

###


class Student:
    # 类 Student，表示一个学生

    ###
    class Scores:
        # 嵌套类 Scores，表示学生的成绩

        def __init__(self, scores):
            # 定义字段表示英语和数学成绩
            self.english = int(scores[0])
            self.math = int(scores[1])

        def sum(self):
            # 计算总成绩
            return self.english + self.math

    ###
    def __init__(self, name, age, scores):
        # 定义字段表示学生的姓名，年龄和成绩
        self.name = name
        self.age = age
        self.scores = self.Scores(scores)

    def show_info(self):
        # 显示学生的信息，包括姓名，年龄和总分数
        print(f'姓名：{self.name} 年龄：{self.age} 总分：{self.scores.sum()}')


### 要求输入学生的相关信息
text = input('请输入姓名和年龄以及成绩，使用空格分割：')

# 使用输入的学生信息，创建 Student 类的实例
args = text.split(' ')
input_name = args[0]
input_age = int(args[1])
input_scores = args[2:]

student = Student(input_name, input_age, input_scores)

### 显示学生的信息
student.show_info()
