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

# 過濾掉使用者輸入的某些詞匯
text = input('請輸入訊息（哈哈，呵呵將被過濾）：')
result = re.sub(r'(哈哈|呵呵)', '**', text)

print(f'過濾後的結果：{result}')