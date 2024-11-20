# 请将命令行跳转至脚本文件 readlines_eof.py 所在的目录，然后运行他
with open('readlines.txt', 'r', encoding='utf8') as file:
    file.read()
    print(f'从文件末尾读取多个行：{file.readlines()}')

with open('readlines.txt', 'rb') as file:
    file.read()
    print(f'从文件末尾读取多个行：{file.readlines()}')