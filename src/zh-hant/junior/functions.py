'''
本節文章
https://learnscript.net/zh-hant/python/junior/define-and-call-functions/ 如何定義和呼叫函式
'''

###


def check_password(password):
    # 函式 check_password 用來檢查密碼的合理性

    if len(password) < 3:
        return False
    else:
        return True


while True:
    pw = input('請輸入密碼登入：')

    # 如果使用者輸入的密碼不合理，或者不等於 'abcd'，則要求重新輸入
    if check_password(pw) and pw == 'abcd':
        print('OK！這次對了！')
        break
    else:
        print('密碼不合理或者密碼錯誤！請重新輸入')

while True:
    pw = input('現在可以修改密碼了，請輸入新的密碼：')

    if check_password(pw):
        print('密碼已經成功修改')
        break
    else:
        print('輸入的新密碼不合理')
