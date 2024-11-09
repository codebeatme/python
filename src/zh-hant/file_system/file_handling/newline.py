# 請將命令列跳躍至腳本檔案 newline.py 所在的目錄，然後執行他

# 函式 read_newline 將采用指定的換行₁方式讀取不同的檔案
def read_newline(nl=None):
    # 依次讀取以 \n，\r\n，\r 為換行₁的檔案
    for name in ('n', 'rn', 'r'):
        fn = f'line_{name}.txt'
        file = open(fn, 'r', encoding='utf8', newline=nl)

        # 顯示檔案中的每一行
        print(file.readlines())


# 采用預設的換行₁處理方式
read_newline()
read_newline('')
read_newline('\n')
read_newline('\r\n')
read_newline('\r')