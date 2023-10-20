'''
本节文章
https://learnscript.net/zh/python/senior/regular-expressions/ 如何使用正则表达式
'''

###
# 导入模块
import re

# 过滤掉用户输入的某些词汇
text = input('请输入消息（哈哈，呵呵将被过滤）：')
result = re.sub(r'(哈哈|呵呵)', '**', text)

print(f'过滤后的结果：{result}')