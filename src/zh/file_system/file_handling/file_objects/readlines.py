# 请将命令行跳转至脚本文件 readlines.py 所在的目录，然后运行他
# 读取文本文件中的多个行
with open('readlines.txt', 'r', encoding='utf8') as file:
    print(f'读取多个行（最多 12 个字符）：{file.readlines(12)}')
    print(f'读取剩余的行：{file.readlines()}')

# 读取二进制文件中的多个行
with open('readlines.txt', 'rb') as file:
    print(f'读取多个行（最多 12 个字节）：{file.readlines(12)}')
    print(f'读取剩余的行：{file.readlines()}')
