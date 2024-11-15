# 请将命令行跳转至脚本文件 readline_eof.py 所在的目录，然后运行他
with open('read.txt', 'r', encoding='utf8') as file:
    file.read()
    print(f'从文件末尾读取一行：{file.readline()}')

with open('read.txt', 'rb') as file:
    file.read()
    print(f'从文件末尾读取一行：{file.readline()}')