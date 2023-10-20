'''
本节文章
https://learnscript.net/zh/python/senior/regular-expressions/ 如何使用正则表达式
'''

###
# 导入模块
import re

# 直到用户输入一个有效的邮箱地址
while True:
    email = input('请输入邮箱地址：')
    # 检查邮箱地址是否有效
    result = re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email)

    # 邮箱地址有效则跳出循环
    if result:
        print('邮箱地址有效')
        break
    else:
        print(f'一个错误的邮箱地址：{email}')
