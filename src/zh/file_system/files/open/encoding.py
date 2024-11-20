# 请将命令行跳转至脚本文件 encoding.py 所在的目录，然后运行他
# 使用编码格式 utf-8 打开文件 utf8.txt
file = open('utf8.txt', 'r', encoding='utf8')
print(file.read())
# 使用编码格式 u8 打开文件 utf8.txt
file = open('utf8.txt', 'r', encoding='u8')
print(file.read())