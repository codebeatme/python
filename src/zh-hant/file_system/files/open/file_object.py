# 請將命令列跳躍至腳本檔案 file_object.py 所在的目錄，然後執行他
# 讀取文字檔案
print(type(open('file_object.txt', 'r')))
# 讀取二進位檔案
print(type(open('file_object.txt', 'rb')))
# 寫入二進位檔案
print(type(open('file_object.txt', 'wb')))
# 讀取及寫入二進位檔案
print(type(open('file_object.txt', 'w+b')))
# 停用緩沖
print(type(open('file_object.txt', 'rb', 0)))