'''
本節文章
https://learnscript.net/zh-hant/python/advanced/get-date-time/ 如何取得日期時間
'''

### 匯入 datetime 模組
import datetime

while True:
    pw = input('請輸入密碼：')

    # 輸入密碼 123456，認為是登入成功
    if pw == '123456':
        # 讀取儲存在 last_login.txt 中的上一次的登入時間
        file_path = 'last_login.txt'

        file = open(file_path, 'r')
        last_time = file.readline()
        file.close()

        # 再次登入時，才會顯示上一次的登入時間
        if last_time:
            print(f'上一次登入時間為 {last_time}')

        # 使用 now 方法取得當前的時間，並將該時間作為登入時間
        last_time = datetime.datetime.now().ctime()

        # 將本次登入時間儲存至 last_login.txt
        file = open(file_path, 'w')
        file.write(last_time)
        file.close()
        break
