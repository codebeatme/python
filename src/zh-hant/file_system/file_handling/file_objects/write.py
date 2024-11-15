# 請將命令列跳躍至腳本檔案 write.py 所在的目錄，然後執行他
# 將字元寫入檔案
with open('write.txt', 'w', encoding='utf8') as file:
    c = file.write('第一行\n第二行')
    print(f'寫入 {c} 個字元')

# 將位元組寫入檔案
with open('writeb.txt', 'wb') as file:
    bs = '第一行\n第二行'.encode()
    print(type(bs))
    c = file.write(bs)
    print(f'寫入 {c} 個位元組')
