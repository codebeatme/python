# 视频内容：「Python」基础教程 如何定义函数？如何调用函数
# 视频地址：https://www.bilibili.com/video/BV1wy4y1o72X/

###
def check_password(password):
    if len(password) < 3:
        return False
    else:
        return True
    
while True:
    pw = input('请输入密码登录：')

    if check_password(pw) and pw == 'abcd':
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
