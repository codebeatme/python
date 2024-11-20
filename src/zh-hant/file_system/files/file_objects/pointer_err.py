# 請將命令列跳躍至腳本檔案 pointer_err.py 所在的目錄，然後執行他
file = open('read.txt', 'r+b')

# 檔案指標位置將超出檔案末尾
file.seek(100, 2)
print(f'指標位置：{file.tell()}')
# 讀取檔案不會產生例外狀況
print(file.read())

# ERROR 檔案指標的位置不能是負數
file.seek(-100, 0)