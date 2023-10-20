'''
本节文章
https://learnscript.net/zh/python/junior/common-data-types/ 常见数据类型有哪些
'''

###
fail_count = 0
allow_input = True

while allow_input:
    ###
    message = f'已经输入错了 {fail_count} 次，请输入密码：'
    pw = input(message)

    ###
    # 如果输入 123456，则认为是糟糕的密码
    if pw == '123456':
        print('这是世界上最糟糕也最常见的密码！')
        # 错误次数加 1，特指输入 123456 的次数
        fail_count += 1

        # 错误次数到达 3，则设置 allow_input 为 False，这将跳出 while 循环
        if fail_count == 3:
            allow_input = False

    else:
        break
