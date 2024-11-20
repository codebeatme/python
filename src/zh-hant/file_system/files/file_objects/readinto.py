# 請將命令列跳躍至腳本檔案 readinto.py 所在的目錄，然後執行他
# 讀取位元組至 bytearray
with open('read.txt', 'rb') as file:
    ba8 = bytearray(8)
    # 嘗試讀取 8 個位元組以填入 ba
    print(f'讀取了 {file.readinto(ba8)} 個位元組')
    print(ba8)

    ba30 = bytearray(30)
    # 讀取剩余的 23 個位元組
    print(f'讀取了 {file.readinto(ba30)} 個位元組')
    print(ba30)