# 视频内容：「Python」高级教程 什么是内部类？如何定义使用内部类
# 视频地址：https://www.bilibili.com/video/BV1zv4y1b7iV/

###
class Student:
    ###
    class Scores:
        def __init__(self, s):
            self.ch = int(s[0])
            self.en = int(s[1])

        def sum(self):
            return self.ch + self.en
        
    ###
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.scores = self.Scores(s)

    def show_info(self):
        print(f'{self.name} 总分 {self.scores.sum()}')

###
text = input('请输入姓名和年龄以及成绩，使用空格分割：')

args = text.split(' ')
input_name = args[0]
input_age = int(args[1])
input_scores = args[2:]

s = Student(input_name, input_age, input_scores)
###
s.show_info()