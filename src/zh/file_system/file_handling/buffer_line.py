# 请将命令行跳转至脚本文件 buffer_line.py 所在的目录，然后运行他
# 启用行缓冲策略
file = open('buffer_line.txt', 'w', 1, encoding='utf8', newline='')

# abc 不会被立即保存至文件
file.writelines(['a', 'b', 'c'])
# abcd\r 会被立即保存至文件
file.write('d\r')
# e\n 会被立即保存至文件
file.write('e\n')
# f\r\n 会被立即保存至文件
file.write('f\r\n')