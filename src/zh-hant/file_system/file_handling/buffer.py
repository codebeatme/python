# 請將命令列跳躍至腳本檔案 buffer.py 所在的目錄，然後執行他
# 設定緩沖區的大小為 2
file = open('buffer_b.txt', 'wb', 2)

# b'1' 將被存放在緩沖區
file.write(b'1')
# b'2' 將被存放在緩沖區
file.write(b'2')
# b'12' 會被立即儲存至檔案，b'3' 將被存放在緩沖區
file.write(b'3')
# b'34567' 會被立即儲存至檔案
file.write(b'4567')



# # 請將命令列跳躍至腳本檔案 buffer_line.py 所在的目錄，然後執行他
# # 設定緩沖區的大小為 2
# file = open('buffer_b.txt', 'wt', encoding='utf8')

# for i in range(1, 8192*2):
#     # b'1' 將被存放在緩沖區
#     file.write('1')
# # b'2' 將被存放在緩沖區
# file.write('a')
# # b'12' 會被立即儲存至檔案，b'3' 將被存放在緩沖區
# file.write('3')
# # b'34567' 會被立即儲存至檔案
# file.write('4567')