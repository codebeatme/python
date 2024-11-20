# 请将命令行跳转至脚本文件 write.py 所在的目录，然后运行他
# 将字符写入文件
with open('write.txt', 'w', encoding='utf8') as file:
    c = file.write('第一行\n第二行')
    print(f'写入 {c} 个字符')

# 将字节写入文件
with open('writeb.txt', 'wb') as file:
    bs = '第一行\n第二行'.encode()
    print(type(bs))
    c = file.write(bs)
    print(f'写入 {c} 个字节')
