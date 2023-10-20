'''
本节文章
https://learnscript.net/zh/python/junior/for-statement/ 如何使用 for 语句
'''

###
students = ['小小', '花花', '明明']

# 教师添加学生，直至输入了 n
while True:
    print('当前名单：', students)

    name = input('请输入学生姓名（输入 n 结束）：')

    if name == 'n':
        break
    else:
        students.append(name)

###
two_count = 0
three_count = 0

# 遍历列表 students 中的所有元素
for name in students:
    # 计算学生姓名的字数，并将对应的变量加 1
    count = len(name)

    if count == 2:
        two_count += 1
    elif count == 3:
        three_count += 1

print(f'两个字的姓名有 {two_count} 个，三个字的姓名有 {three_count} 个')
