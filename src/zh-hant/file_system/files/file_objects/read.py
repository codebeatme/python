# 請將命令列跳躍至腳本檔案 read.py 所在的目錄，然後執行他
# 讀取檔案中的字元
with open('read.txt', 'r', encoding='utf8') as file:
    print(f'讀取 4 個字元：{file.read(4)}')
    print(f'讀取剩余字元：{file.read()}')

# 讀取檔案中的位元組
with open('read.txt', 'rb') as file:
    print(f'讀取 4 個位元組：{file.read(4)}')
    print(f'讀取剩余位元組：{file.read()}')

# 讀取檔案中的位元組，但停用緩沖區
with open('read.txt', 'rb', buffering=0) as file:
    print(f'讀取 4 個位元組：{file.read(4)}')
    print(f'讀取剩余位元組：{file.readall()}')