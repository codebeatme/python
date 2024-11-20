# 請將命令列跳躍至腳本檔案 readline.py 所在的目錄，然後執行他
# 讀取文字檔案中的行
with open('read.txt', 'r', encoding='utf8') as file:
    print(f'讀取 4 個字元：{file.read(4)}')
    # 包括 \n
    print(f'讀取行：{file.readline()}')
    print(f'讀取行（最多 2 個字元）：{file.readline(2)}')
    print(f'讀取行：{file.readline()}')

# 讀取二進位檔案中的行
with open('read.txt', 'rb') as file:
    print(f'讀取 4 個位元組：{file.read(4)}')
    # 包括 \r\n
    print(f'讀取行：{file.readline()}')
    print(f'讀取行（最多 2 個位元組）：{file.readline(2)}')
    print(f'讀取行：{file.readline()}')