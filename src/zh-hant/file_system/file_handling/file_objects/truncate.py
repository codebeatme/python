# 請將命令列跳躍至腳本檔案 truncate.py 所在的目錄，然後執行他
with open('truncate.txt', 'r+', encoding="utf8") as file:
    # 顯示檔案內容
    print(file.read())
    # 保留“真是美好”
    print(f'從第 12 個位元組處截斷：{file.truncate(12)}')
    # 檔案指標位置不會被 truncate 方法改變
    print(f'目前指標位置：{file.tell()}')