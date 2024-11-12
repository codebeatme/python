# 请将命令行跳转至脚本文件 buffer.py 所在的目录，然后运行他
# 设置缓冲区的大小为 2
file = open('buffer_b.txt', 'wb', 2)

# b'1' 将被存放在缓冲区
file.write(b'1')
# b'2' 将被存放在缓冲区
file.write(b'2')
# b'12' 会被立即保存至文件，b'3' 将被存放在缓冲区
file.write(b'3')
# b'34567' 会被立即保存至文件
file.write(b'4567')



# # 请将命令行跳转至脚本文件 buffer_line.py 所在的目录，然后运行他
# # 设置缓冲区的大小为 2
# file = open('buffer_b.txt', 'wt', encoding='utf8')

# for i in range(1, 8192*2):
#     # b'1' 将被存放在缓冲区
#     file.write('1')
# # b'2' 将被存放在缓冲区
# file.write('a')
# # b'12' 会被立即保存至文件，b'3' 将被存放在缓冲区
# file.write('3')
# # b'34567' 会被立即保存至文件
# file.write('4567')