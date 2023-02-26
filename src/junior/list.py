###
students = ['小小', '花花', '明明']

###
while True:
    print('当前名单：', students)

    name = input('请输入学生姓名（输入n结束）：')

    if name == 'n':
        break
    else:
        students.append(name)  