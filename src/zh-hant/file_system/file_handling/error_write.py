# 請將命令列跳躍至腳本檔案 error_write.py 所在的目錄，然後執行他

# 函式 write 將開啟檔案並寫入一些內容
def write(e):
    try:
        file = open(f'error_{e}.txt', 'w', encoding='ascii', errors=e)
        # 將內容寫入檔案
        file.write('今天 is good')
    except Exception as err:
        print(f'{e} {err}')


# 使用不同的錯誤處理方式寫入檔案
write('strict')
write('ignore')
write('replace')
write('backslashreplace')
write('xmlcharrefreplace')
write('namereplace')

# 檢視檔案中被寫入的內容
for i in ('strict', 'ignore', 'replace', 'backslashreplace', 'xmlcharrefreplace', 'namereplace'):
    fn = f'error_{i}.txt'
    file = open(fn, 'r', encoding='ascii')
    print(f'{fn} {file.read()}')
