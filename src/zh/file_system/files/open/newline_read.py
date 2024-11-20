# 请将命令行跳转至脚本文件 newline_read.py 所在的目录，然后运行他

# 函数 read_newline 将采用指定的换行₁方式读取不同的文件
def read_newline(nl=None):
    # 依次读取以 \n，\r\n，\r 为换行₁的文件
    for name in ('n', 'rn', 'r'):
        fn = f'line_{name}.txt'
        file = open(fn, 'r', encoding='utf8', newline=nl)

        # 显示文件中的每一行
        print(file.readlines())


# 采用不同的换行₁方式读取不同的文件
read_newline()
read_newline('')
read_newline('\n')
read_newline('\r\n')
read_newline('\r')