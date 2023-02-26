###
fail_count = 0
allow_input = True

while allow_input:
    ###
    message = f'''已经输入错了{fail_count}次
    请输入密码：'''
    pw = input(message)

    ###
    if pw == '123456':
        print('这是世界上最糟糕也最常见的密码！')
        fail_count += 1

        if fail_count == 3:
            allow_input = False

    elif pw == 'password':
        print('这个密码和123456一样糟糕！')
    else:
        print('这是很好的密码！')
        break