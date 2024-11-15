# 请将命令行跳转至脚本文件 pointer.py 所在的目录，然后运行他
file = open('read.txt', 'r', encoding='utf8')

# 开始时指针位于文件开头
print(f'指针位置：{file.tell()}')
# 将指针移动到“你好”之后，“你好”占用了 6 个字节
file.seek(6, 0)
# 读取下一个字符“，”
print(file.read(1))
# 由于“，”占用 3 个字节，因此指针位置现在为 9
print(f'指针位置：{file.tell()}')