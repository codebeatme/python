# 請將命令列跳躍至腳本檔案 encoding.py 所在的目錄，然後執行他
# 使用編碼格式 utf-8 開啟檔案 utf8.txt
file = open('utf8.txt', 'r', encoding='utf8')
print(file.read())
# 使用編碼格式 u8 開啟檔案 utf8.txt
file = open('utf8.txt', 'r', encoding='u8')
print(file.read())