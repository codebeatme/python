'''
本節文章
https://learnscript.net/zh-hant/python/junior/set/ 什麽是集合？集合和串列有何不同
'''

###
numbers = set()

numbers.add(3)
numbers.add(1)
numbers.add(5)
numbers.add(4)
numbers.add(2)

# 將按照 1 2 3 4 5 的順序顯示
print(numbers)

###
students = {'小小', '花花', '明明'}

###
while True:
    name = input('請輸入學生姓名（輸入 n 結束）：')

    # 如果學生已經在集合 students 中，則不會添加
    if name in students:
        print(f'姓名 {name} 已經存在')
    elif name == 'n':
        print(students)
        break
    else:
        students.add(name)
