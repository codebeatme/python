# 請將命令列跳躍至腳本檔案 readlines.py 所在的目錄，然後執行他
# 讀取文字檔案中的多個行
with open('readlines.txt', 'r', encoding='utf8') as file:
    print(f'讀取多個行（最多 12 個字元）：{file.readlines(12)}')
    print(f'讀取剩余的行：{file.readlines()}')

# 讀取二進位檔案中的多個行
with open('readlines.txt', 'rb') as file:
    print(f'讀取多個行（最多 12 個位元組）：{file.readlines(12)}')
    print(f'讀取剩余的行：{file.readlines()}')
