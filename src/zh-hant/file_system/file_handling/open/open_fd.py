# 請將命令列跳躍至腳本檔案 open_fd.py 所在的目錄，然後執行他
# 使用 os 模組的 open 函式建立檔案描述器
import os
fd = os.open('info.txt', os.O_RDONLY)

# 使用檔案描述器開啟檔案
file = open(fd, encoding='utf8', closefd=False)
print(file.read())

# 不會同時關閉檔案描述器
file.close()
# 可以使用檔案描述器再次開啟檔案
open(fd, encoding='utf8')