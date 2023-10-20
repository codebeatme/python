'''
本节文章
https://learnscript.net/zh/python/junior/dict/ 什么是字典
'''
table = {'name': '-', 'age': 0}

# 如果姓名和年龄不再是初始值，则认为他们已经被正确输入
while table['name'] == '-' or table['age'] == 0:
    my_name = input('请输入您的姓名：')
    my_age = input('请输入您的年龄：')

    # 输入的内容不为空，才被认为是正确的
    if my_name:
        table['name'] = my_name

    if my_age:
        table['age'] = int(my_age)

    print(table)
