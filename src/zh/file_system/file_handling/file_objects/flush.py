# 请将命令行跳转至脚本文件 flush.py 所在的目录，然后运行他
with open('flush.txt', 'wb', buffering=4) as file:
    file.write(b'abc')
    # 将缓冲区中的 abc 写入文件
    file.flush()