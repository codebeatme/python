# 请将命令行跳转至脚本文件 file_object.py 所在的目录，然后运行他
# 读取文本文件
print(type(open('file_object.txt', 'r')))
# 读取二进制文件
print(type(open('file_object.txt', 'rb')))
# 写入二进制文件
print(type(open('file_object.txt', 'wb')))
# 读写二进制文件
print(type(open('file_object.txt', 'w+b')))
# 禁用缓冲
print(type(open('file_object.txt', 'rb', 0)))