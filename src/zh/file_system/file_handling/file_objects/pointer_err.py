# 请将命令行跳转至脚本文件 pointer_err.py 所在的目录，然后运行他
file = open('read.txt', 'r+b')

# 文件指针位置将超出文件末尾
file.seek(100, 2)
print(f'指针位置：{file.tell()}')
# 读取文件不会产生异常
print(file.read())

# ERROR 文件指针的位置不能是负数
file.seek(-100, 0)