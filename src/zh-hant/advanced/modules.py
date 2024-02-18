'''
本節文章
https://learnscript.net/zh-hant/python/advanced/create-and-import-modules/ 如何建立，匯入，使用模組
'''

# 匯入 info 模組
import info

# 使用 . 運算子呼叫模組中的函式 welcome
message = info.welcome()

print(message)