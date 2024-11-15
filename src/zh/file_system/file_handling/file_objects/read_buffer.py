# 请将命令行跳转至脚本文件 read_buffer.py 所在的目录，然后运行他
# 读取缓冲区中的字节
with open('read.txt', 'rb', buffering=3) as file:
    print(f'读取 4 个字节？{file.read1(8)}')
    # 由于缓冲区大小为 3，因此最多读取三个字符
    print(f'读取剩余字节？{file.read1()}')

    ba = bytearray(8)
    print(file.readinto1(ba))