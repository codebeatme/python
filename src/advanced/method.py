###
class Student:

    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.scores = s

    def sum_score(self):
        total = 0

        for score in self.scores:
            total += int(score)

        return total

###
students = []

while True:
    text = input('请输入姓名和年龄以及成绩，使用空格分割：')

    if text == 'n':
        break

    ###
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])
    input_scores = args[2:]

    student = Student(input_name, input_age, input_scores)

    students.append(student)

###
for s in students:
    total_score = s.sum_score()
    print(f'学生{s.name} 年龄{s.age} 成绩{total_score}')