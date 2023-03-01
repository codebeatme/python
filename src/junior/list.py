# 视频内容：「Python」基础教程 如何更好的理解列表和元组
# 视频地址：https://www.bilibili.com/video/BV1ay4y1Q7Lt/

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
