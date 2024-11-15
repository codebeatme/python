# 請將命令列跳躍至腳本檔案 for.py 所在的目錄，然後執行他
# 使用 for 陳述式周遊檔案
with open('readlines.txt', 'r', encoding='utf8') as file:
    for l in file:
        print(l)