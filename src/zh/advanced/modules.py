'''
本节文章
https://learnscript.net/zh/python/advanced/create-and-import-modules/ 如何创建，导入，使用模块
'''

# 导入 info 模块
import info

# 使用 . 运算符调用模块中的函数 welcome
message = info.welcome()

print(message)
