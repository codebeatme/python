# 請將命令列跳躍至腳本檔案 error_read.py 所在的目錄，然後執行他

# 函式 read 將開啟檔案並讀取其中的內容
def read(e):
    try:
        file = open('error.txt', 'r', encoding='ascii', errors=e)
        # 顯示檔案中的內容
        text = file.read()
        print(f'{e} {text}')
    except Exception as err:
        print(f'{e} {err}')

# 使用不同的錯誤處理方式讀取檔案 error.txt
read('strict')
read('ignore')
read('replace')
read('backslashreplace')
# read('xmlcharrefreplace')
# read('namereplace')
# read('surrogateescape')
