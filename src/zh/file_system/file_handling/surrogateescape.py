# 请将命令行跳转至脚本文件 surrogateescape.py 所在的目录，然后运行他
# 尝试将 \udc80\udc81\udc82 写入文件 surrogate.txt
file = open('surrogate.txt', 'w', encoding='utf8', errors='surrogateescape')
file.write('\udc80\udc81\udc82')

# 读取文件 surrogate.txt 中的内容，并显示其 Unicode 编码值
file = open('surrogate.txt', 'r', encoding='utf8', errors='surrogateescape')
for c in file.read():
    print(hex(ord(c)))