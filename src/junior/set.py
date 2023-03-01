# 视频内容：「Python」基础教程 集合与列表的区别是什么？以及简单运用
# 视频地址：https://www.bilibili.com/video/BV1Dj411N7JA/

###
students = {'小小', '花花', '明明'}

###
while True:
    name = input('请输入学生姓名（输入n结束）：')

    if name in students:
        print(f'姓名{name}已经存在')
    elif name == 'n':
        print(students)
        break
    else:
        students.add(name)
