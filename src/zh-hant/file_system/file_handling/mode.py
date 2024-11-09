# 請將命令列跳躍至腳本檔案 mode.py 所在的目錄，然後執行他
# 可以對檔案進行讀取及寫入，若檔案不存在則引發例外狀況
file = open('info.txt', 'r+', encoding='utf8')

# 讀取檔案中的行
print(file.readlines())
# 寫入新的行
file.writelines(['\n這是新的一行'])

# 需要 r，w，a，x 中的一個
try: open('info.txt', 't', encoding='utf8')
except ValueError as e: print(e)
# r，w，a，x 不能同時出現
try: open('info.txt', 'rw', encoding='utf8')
except ValueError as e: print(e)