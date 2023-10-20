'''
本节文章
https://learnscript.net/zh/python/junior/list-and-tuple/ 什么是列表，元组？有何不同
'''

###
students = ('小小', '花花', '明明')

###
name = input('请输入要查询的学生姓名：')

# 根据学生是否在元组 students 中，显示不同的信息
if name in students:
    print('在名单中找到了该学生')
else:
    print('名单中找不到该学生')
