# 视频内容：「Python」基础教程 什么是字典？字典的书写格式
# 视频地址：https://www.bilibili.com/video/BV1954y1N7cD/

table = {'name': '-', 'age': 0}

while table['name'] == '-' or table['age'] == 0:
    my_name = input('请输入您的姓名：')
    my_age = input('请输入您的年龄：')

    if my_name:
        table['name'] = my_name

    if my_age:
        table['age'] = int(my_age)

    print(table)
