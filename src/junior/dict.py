table = {'name': '-', 'age': 0}

while table['name'] == '-' or table['age'] == 0:
    my_name = input('请输入您的姓名：')
    my_age = input('请输入您的年龄：')

    if my_name:
        table['name'] = my_name

    if my_age:
        table['age'] = int(my_age)

    print(table)