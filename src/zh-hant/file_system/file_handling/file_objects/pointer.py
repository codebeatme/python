# 請將命令列跳躍至腳本檔案 pointer.py 所在的目錄，然後執行他
file = open('read.txt', 'r', encoding='utf8')

# 開始時指標位於檔案開頭
print(f'指標位置：{file.tell()}')
# 將指標移動到“你好”之後，“你好”占用了 6 個位元組
file.seek(6, 0)
# 讀取下一個字元“，”
print(file.read(1))
# 由於“，”占用 3 個位元組，因此指標位置現在為 9
print(f'指標位置：{file.tell()}')