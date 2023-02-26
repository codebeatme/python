###
students = ['小小', '花花', '明明']

while True:
    print('当前名单：', students)

    name = input('请输入学生姓名（输入n结束）：')

    if name == 'n':
        break
    else:
        students.append(name)

###
two_words_count = 0
three_words_count = 0

for name in students:
    words_count = len(name)

    if words_count == 2:
        two_words_count += 1
    elif words_count == 3:
        three_words_count += 1

print(f'两个字的姓名有{two_words_count}个，三个字的姓名有{three_words_count}个')