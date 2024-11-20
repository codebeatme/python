# 請將命令列跳躍至腳本檔案 read_eof.py 所在的目錄，然後執行他
with open('read.txt', 'r', encoding='utf8') as file:
    file.read()
    print(f'從檔案末尾讀取字元：{file.read()}')

with open('read.txt', 'rb') as file:
    file.read()
    print(f'從檔案末尾讀取位元組：{file.read()}')