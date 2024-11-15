# 請將命令列跳躍至腳本檔案 closed.py 所在的目錄，然後執行他
# with 陳述式結束之後，檔案將被關閉
with open('close.txt', 'w', encoding='utf8') as file:
    file.write('寫入一些資料！')

# 檢查檔案是否被關閉
if file.closed:
    print('檔案 close.txt 已經關閉')