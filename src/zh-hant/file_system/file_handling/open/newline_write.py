# 請將命令列跳躍至腳本檔案 newline_write.py 所在的目錄，然後執行他
no = 1

# 采用不同的換行₁方式寫入相同的內容
for nl in (None, '', '\n', '\r\n', '\r'):
    fn = f'line_w_{no}.txt'
    file = open(fn, 'w', encoding='utf8', newline=nl)
    file.writelines(['\n', '\r\n', '\r'])

    no += 1

# 檢視檔案中被寫入的內容
for i in range(1, 6):
    file = open(f'line_w_{i}.txt', 'r', encoding='utf8', newline='')
    print(file.read().encode())