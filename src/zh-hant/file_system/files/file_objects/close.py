# 請將命令列跳躍至腳本檔案 close.py 所在的目錄，然後執行他
file = open('close.txt', 'w', encoding='utf8')
file.write('寫入一些資料！')
# 關閉檔案
file.close()

# ERROR 檔案已經關閉
file.write('再寫入一些資料？')