###
students = ('小小', '花花', '明明')

###
name = input('请输入要查询的学生姓名：')

if name in students:
    print('在名单中找到了该学生')
else:
    print('名单中找不到该学生')