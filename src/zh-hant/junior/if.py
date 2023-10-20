'''
本節文章
https://learnscript.net/zh-hant/python/junior/if-statement/ 如何使用 if 陳述式
'''

###
fail_count = 0
allow_input = True

while allow_input:
    ###
    message = f'已經輸入錯了 {fail_count} 次，請輸入密碼：'
    pw = input(message)

    ###
    # 判斷 pw 是否等於 '123456'
    if pw == '123456':
        print('這是世界上最糟糕也最常見的密碼！')
        fail_count += 1

        if fail_count == 3:
            allow_input = False

    # 如果 pw 不等於 '123456'，則判斷 pw 是否等於 'password'
    elif pw == 'password':
        print('這個密碼和 123456 一樣糟糕！')
    # 如果 pw 既不等於 '123456'，也不等於 'password'，則執行
    else:
        print('這是很好的密碼！')
        break
