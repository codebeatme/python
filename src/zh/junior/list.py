'''
本节文章
https://learnscript.net/zh/python/junior/list-and-tuple/ 什么是列表，元组？有何不同
'''

###
students = ['小小', '花花', '明明']

###
while True:
    print('当前名单：', students)

    name = input('请输入学生姓名（输入 n 结束）：')

    # 输入 n，执行 break 语句跳出循环，否则将添加学生到 students 列表
    if name == 'n':
        break
    else:
        students.append(name)
