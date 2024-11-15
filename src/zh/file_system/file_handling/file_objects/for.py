# 请将命令行跳转至脚本文件 for.py 所在的目录，然后运行他
# 使用 for 语句遍历文件
with open('readlines.txt', 'r', encoding='utf8') as file:
    for l in file:
        print(l)