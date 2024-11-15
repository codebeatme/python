# 请将命令行跳转至脚本文件 read_eof.py 所在的目录，然后运行他
with open('read.txt', 'r', encoding='utf8') as file:
    file.read()
    print(f'从文件末尾读取字符：{file.read()}')

with open('read.txt', 'rb') as file:
    file.read()
    print(f'从文件末尾读取字节：{file.read()}')