# 請將命令列跳躍至腳本檔案 surrogateescape.py 所在的目錄，然後執行他
# 嘗試將 \udc80\udc81\udc82 寫入檔案 surrogate.txt
file = open('surrogate.txt', 'w', encoding='utf8', errors='surrogateescape')
file.write('\udc80\udc81\udc82')

# 讀取檔案 surrogate.txt 中的內容，並顯示其 Unicode 編碼值
file = open('surrogate.txt', 'r', encoding='utf8', errors='surrogateescape')
for c in file.read():
    print(hex(ord(c)))