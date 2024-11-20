# 請將命令列跳躍至腳本檔案 info.py 所在的目錄，然後執行他
with open('read.txt', 'r', encoding='utf8') as file:
	print(f'讀取：{file.readable()}，寫入：{file.writable()}')

with open('read.txt', 'r+b') as file:
	print(f'讀取：{file.readable()}，寫入：{file.writable()}')
      
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
