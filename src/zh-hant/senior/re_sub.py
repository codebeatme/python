'''
本節文章
https://learnscript.net/zh-hant/python/senior/regular-expressions/ 如何使用規則運算式
'''

###
# 匯入模組
import re

# 過濾掉使用者輸入的某些詞匯
text = input('請輸入訊息（哈哈，呵呵將被過濾）：')
result = re.sub(r'(哈哈|呵呵)', '**', text)

print(f'過濾後的結果：{result}')