'''
本节文章
https://learnscript.net/zh/python/junior/set/ 什么是集合？集合和列表有何不同
'''

###
numbers = set()

numbers.add(3)
numbers.add(1)
numbers.add(5)
numbers.add(4)
numbers.add(2)

# 将按照 1 2 3 4 5 的顺序显示
print(numbers)

###
students = {'小小', '花花', '明明'}

###
while True:
    name = input('请输入学生姓名（输入 n 结束）：')

    # 如果学生已经在集合 students 中，则不会添加
    if name in students:
        print(f'姓名 {name} 已经存在')
    elif name == 'n':
        print(students)
        break
    else:
        students.add(name)
