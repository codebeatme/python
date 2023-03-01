# 视频内容：「Python」基础教程 怎么样理解数字，字符串与布尔值
# 视频地址：https://www.bilibili.com/video/BV1y8411M7zg/

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

    else:
        break
