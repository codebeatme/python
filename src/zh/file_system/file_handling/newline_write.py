# 请将命令行跳转至脚本文件 newline_write.py 所在的目录，然后运行他
no = 1

# 采用不同的换行₁方式写入相同的内容
for nl in (None, '', '\n', '\r\n', '\r'):
    fn = f'line_w_{no}.txt'
    file = open(fn, 'w', encoding='utf8', newline=nl)
    file.writelines(['\n', '\r\n', '\r'])

    no += 1

# 查看文件中被写入的内容
for i in range(1, 6):
    file = open(f'line_w_{i}.txt', 'r', encoding='utf8', newline='')
    print(file.read().encode())