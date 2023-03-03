# 视频内容：「Python」进阶教程 如何使用datetime获取当前日期时间
# 视频地址：https://www.bilibili.com/video/BV16N411F7ko/

import datetime
import os

while True:
    pw = input('请输入密码：')

    if pw == '123456':
        file_path = os.path.abspath('src/advanced/last_login.txt')

        file = open(file_path, 'r')
        last_time = file.readline()
        file.close()

        if last_time:
            print(f'上一次登录时间为{last_time}')

        last_time = datetime.datetime.now().ctime()

        file = open(file_path, 'w')
        file.write(last_time)
        file.close()
        break