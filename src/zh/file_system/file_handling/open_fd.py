# 请将命令行跳转至脚本文件 open_fd.py 所在的目录，然后运行他
# 使用 os 模块的 open 函数创建文件描述器
import os
fd = os.open('info.txt', os.O_RDONLY)

# 使用文件描述器打开文件
file = open(fd, encoding='utf8', closefd=False)
print(file.read())

# 不会同时关闭文件描述器
file.close()
# 可以使用文件描述器再次打开文件
open(fd, encoding='utf8')