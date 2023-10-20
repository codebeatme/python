'''
規則運算式可用來判斷字串是否匹配某種規則，或尋找取代字串中匹配規則的內容
* match函式可判斷整個字串是否匹配規則
* search函式可尋找字串中匹配規則的部分
* sub函式可取代字串中匹配規則的部分

版本
Python 3.11.2
VSCode 1.76.1

關於本系列教程的使用說明和相關問題解答，請參考文章 https://www.bilibili.com/read/cv23030766
'''

###
# 匯入模組
import re

# 直到使用者輸入一個有效的電子郵件地址
while True:
    email = input('請輸入電子郵件地址：')
    # 檢查電子郵件地址是否有效
    result = re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email)

    # 電子郵件地址有效則跳出迴圈
    if result:
        print('電子郵件地址有效')
        break
    else:
        print(f'一個錯誤的電子郵件地址：{email}')
