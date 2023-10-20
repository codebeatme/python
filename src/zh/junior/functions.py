'''
本节文章
https://learnscript.net/zh/python/junior/define-and-call-functions/ 如何定义和调用函数
'''

###


def check_password(password):
    # 函数 check_password 用来检查密码的合理性

    if len(password) < 3:
        return False
    else:
        return True


while True:
    pw = input('请输入密码登录：')

    # 如果用户输入的密码不合理，或者不等于 'abcd'，则要求重新输入
    if check_password(pw) and pw == 'abcd':
        print('OK！这次对了！')
        break
    else:
        print('密码不合理或者密码错误！请重新输入')

while True:
    pw = input('现在可以修改密码了，请输入新的密码：')

    if check_password(pw):
        print('密码已经成功修改')
        break
    else:
        print('输入的新密码不合理')
