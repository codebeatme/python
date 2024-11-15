# 请将命令行跳转至脚本文件 readline.py 所在的目录，然后运行他
# 读取文本文件中的行
with open('read.txt', 'r', encoding='utf8') as file:
    print(f'读取 4 个字符：{file.read(4)}')
    # 包括 \n
    print(f'读取行：{file.readline()}')
    print(f'读取行（最多 2 个字符）：{file.readline(2)}')
    print(f'读取行：{file.readline()}')

# 读取二进制文件中的行
with open('read.txt', 'rb') as file:
    print(f'读取 4 个字节：{file.read(4)}')
    # 包括 \r\n
    print(f'读取行：{file.readline()}')
    print(f'读取行（最多 2 个字节）：{file.readline(2)}')
    print(f'读取行：{file.readline()}')