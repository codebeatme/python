# 請將命令列跳躍至腳本檔案 flush.py 所在的目錄，然後執行他
with open('flush.txt', 'wb', buffering=4) as file:
    file.write(b'abc')
    # 將緩沖區中的 abc 寫入檔案
    file.flush()