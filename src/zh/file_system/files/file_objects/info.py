# 请将命令行跳转至脚本文件 info.py 所在的目录，然后运行他
with open('read.txt', 'r', encoding='utf8') as file:
	print(f'读取：{file.readable()}，写入：{file.writable()}')

with open('read.txt', 'r+b') as file:
	print(f'读取：{file.readable()}，写入：{file.writable()}')
      
with open('read.txt', 'r', encoding='utf8') as file:
    print(f'name {file.name}')
    print(f'fileno {file.fileno()}')
    print(f'mode {file.mode}')
    print(f'encoding {file.encoding}')
    print(f'errors {file.errors}')
    print(f'line_buffering {file.line_buffering}')

import os
fd = os.open('read.txt', os.O_RDONLY | os.O_BINARY)
with open(fd, 'rb', buffering=0, closefd=False) as file:
    print(f'name {file.name}')
    print(f'closefd {file.closefd}')
