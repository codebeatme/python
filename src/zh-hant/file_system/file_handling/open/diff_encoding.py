# 請將命令列跳躍至腳本檔案 diff_encoding.py 所在的目錄，然後執行他
# 使用編碼格式 ascii 開啟編碼格式為 utf8 的檔案 diff.txt
file = open('diff.txt', 'r+', encoding='ascii')

# 無法讀取與 ascii 不相容的 utf8 字元
try: file.readline()
except UnicodeDecodeError as e: print(e)
# 無法寫入與 ascii 不相容的 utf8 字元
try: file.write('你好！')
except UnicodeEncodeError as e: print(e)

# 可以寫入 ascii 字元
file.writelines(['\nHello!'])
# 檔案 diff.txt 被儲存之後，編碼格式依然為 utf8