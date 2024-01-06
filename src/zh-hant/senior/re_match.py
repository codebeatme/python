'''
本節文章
https://learnscript.net/zh-hant/python/senior/regular-expressions/ 如何使用規則運算式
'''

###
# 匯入模組
import re

# 直到使用者輸入一個有效的電子郵件位址
while True:
    email = input('請輸入電子郵件位址：')
    # 檢查電子郵件位址是否有效
    result = re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email)

    # 電子郵件位址有效則跳出迴圈
    if result:
        print('電子郵件位址有效')
        break
    else:
        print(f'一個錯誤的電子郵件位址：{email}')
