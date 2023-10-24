'''
本节文章
https://learnscript.net/zh/python/advanced/get-date-time/ 如何获取日期时间
'''

### 导入 datetime 模块
import datetime

while True:
    pw = input('请输入密码：')

    # 输入密码 123456，认为是登录成功
    if pw == '123456':
        # 读取保存在 last_login.txt 中的上一次的登录时间
        file_path = 'last_login.txt'

        file = open(file_path, 'r')
        last_time = file.readline()
        file.close()

        # 再次登录时，才会显示上一次的登录时间
        if last_time:
            print(f'上一次登录时间为 {last_time}')

        # 使用 now 方法获取当前的时间，并将该时间作为登录时间
        last_time = datetime.datetime.now().ctime()

        # 将本次登录时间保存至 last_login.txt
        file = open(file_path, 'w')
        file.write(last_time)
        file.close()
        break
