# 请将命令行跳转至脚本文件 read.py 所在的目录，然后运行他
# 读取文件中的字符
with open('read.txt', 'r', encoding='utf8') as file:
    print(f'读取 4 个字符：{file.read(4)}')
    print(f'读取剩余字符：{file.read()}')

# 读取文件中的字节
with open('read.txt', 'rb') as file:
    print(f'读取 4 个字节：{file.read(4)}')
    print(f'读取剩余字节：{file.read()}')

# 读取文件中的字节，但禁用缓冲区
with open('read.txt', 'rb', buffering=0) as file:
    print(f'读取 4 个字节：{file.read(4)}')
    print(f'读取剩余字节：{file.readall()}')