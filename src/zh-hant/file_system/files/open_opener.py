# 請將命令列跳躍至腳本檔案 open_opener.py 所在的目錄，然後執行他
import os

# 只會傳回用於讀取操作的檔案描述器
def myopener(file, flags):
    print(f'file {file} flags {flags}')
    return os.open(file, os.O_RDONLY)

# 無論選擇哪種開啟模式，檔案都是唯讀的
file = open('opener.txt', 'r', encoding='utf8', opener=myopener)
print(file.read())
file = open('opener.txt', 'w', encoding='utf8', opener=myopener)
# 雖然沒有例外狀況發生，但檔案 opener.txt 中的內容不會發生變化
file.write('寫點東西')