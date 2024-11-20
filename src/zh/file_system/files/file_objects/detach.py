# 请将命令行跳转至脚本文件 detach.py 所在的目录，然后运行他
with open('read.txt', 'rb', buffering=0) as file:
    print(file.read(1))
    print(file.readall())