'''
本节文章
https://learnscript.net/zh/python/junior/if-statement/ 如何使用 if 语句
'''

###
fail_count = 0
allow_input = True

while allow_input:
    ###
    message = f'已经输入错了 {fail_count} 次，请输入密码：'
    pw = input(message)

    ###
    # 判断 pw 是否等于 '123456'
    if pw == '123456':
        print('这是世界上最糟糕也最常见的密码！')
        fail_count += 1

        if fail_count == 3:
            allow_input = False

    # 如果 pw 不等于 '123456'，则判断 pw 是否等于 'password'
    elif pw == 'password':
        print('这个密码和 123456 一样糟糕！')
    # 如果 pw 既不等于 '123456'，也不等于 'password'，则执行
    else:
        print('这是很好的密码！')
        break
