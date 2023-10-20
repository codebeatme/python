'''
本節文章
https://learnscript.net/zh-hant/python/junior/dict/ 什麽是字典
'''
table = {'name': '-', 'age': 0}

# 如果姓名和年齡不再是初始值，則認為他們已經被正確輸入
while table['name'] == '-' or table['age'] == 0:
    my_name = input('請輸入您的姓名：')
    my_age = input('請輸入您的年齡：')

    # 輸入的內容不為空，才被認為是正確的
    if my_name:
        table['name'] = my_name

    if my_age:
        table['age'] = int(my_age)

    print(table)
