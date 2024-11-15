# 請將命令列跳躍至腳本檔案 readlines_eof.py 所在的目錄，然後執行他
with open('readlines.txt', 'r', encoding='utf8') as file:
    file.read()
    print(f'從檔案末尾讀取多個行：{file.readlines()}')

with open('readlines.txt', 'rb') as file:
    file.read()
    print(f'從檔案末尾讀取多個行：{file.readlines()}')