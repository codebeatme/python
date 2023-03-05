###
class Student:
    ###
        
    ###
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.scores = s

###
text = input('请输入姓名和年龄以及成绩，使用空格分割：')

args = text.split(' ')
input_name = args[0]
input_age = int(args[1])
input_scores = args[2:]

s = Student(input_name, input_age, input_scores)
###
