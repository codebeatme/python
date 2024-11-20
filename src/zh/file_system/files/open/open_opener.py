# 请将命令行跳转至脚本文件 open_opener.py 所在的目录，然后运行他
import os

# 只会返回用于读取操作的文件描述器
def myopener(file, flags):
    print(f'file {file} flags {flags}')
    return os.open(file, os.O_RDONLY)

# 无论选择哪种打开模式，文件都是只读的
file = open('opener.txt', 'r', encoding='utf8', opener=myopener)
print(file.read())
file = open('opener.txt', 'w', encoding='utf8', opener=myopener)
# 虽然没有异常发生，但文件 opener.txt 中的内容不会发生变化
file.write('写点东西')