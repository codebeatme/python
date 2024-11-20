# 請將命令列跳躍至腳本檔案 buffer_line.py 所在的目錄，然後執行他
# 啟用行緩沖策略
file = open('buffer_line.txt', 'w', 1, encoding='utf8', newline='')

# abc 不會被立即儲存至檔案
file.writelines(['a', 'b', 'c'])
# abcd\r 會被立即儲存至檔案
file.write('d\r')
# e\n 會被立即儲存至檔案
file.write('e\n')
# f\r\n 會被立即儲存至檔案
file.write('f\r\n')