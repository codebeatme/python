# 请将命令行跳转至脚本文件 readinto.py 所在的目录，然后运行他
# 读取字节至 bytearray
with open('read.txt', 'rb') as file:
    ba8 = bytearray(8)
    # 尝试读取 8 个字节以填充 ba
    print(f'读取了 {file.readinto(ba8)} 个字节')
    print(ba8)

    ba30 = bytearray(30)
    # 读取剩余的 23 个字节
    print(f'读取了 {file.readinto(ba30)} 个字节')
    print(ba30)