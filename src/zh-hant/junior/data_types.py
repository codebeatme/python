'''
本節文章
https://learnscript.net/zh-hant/python/junior/common-data-types/ 常見資料型別有哪些
'''

###
fail_count = 0
allow_input = True

while allow_input:
    ###
    message = f'已經輸入錯了 {fail_count} 次，請輸入密碼：'
    pw = input(message)

    ###
    # 如果輸入 123456，則認為是糟糕的密碼
    if pw == '123456':
        print('這是世界上最糟糕也最常見的密碼！')
        # 錯誤次數加 1，特指輸入 123456 的次數
        fail_count += 1

        # 錯誤次數到達 3，則設定 allow_input 為 False，這將跳出 while 迴圈
        if fail_count == 3:
            allow_input = False

    else:
        break
