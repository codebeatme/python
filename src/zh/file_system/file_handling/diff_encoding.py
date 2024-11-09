# 请将命令行跳转至脚本文件 diff_encoding.py 所在的目录，然后运行他
# 使用编码格式 ascii 打开编码格式为 utf8 的文件 diff.txt
file = open('diff.txt', 'r+', encoding='ascii')

# 无法读取与 ascii 不兼容的 utf8 字符
try: file.readline()
except UnicodeDecodeError as e: print(e)
# 无法写入与 ascii 不兼容的 utf8 字符
try: file.write('你好！')
except UnicodeEncodeError as e: print(e)

# 可以写入 ascii 字符
file.writelines(['\nHello!'])
# 文件 diff.txt 被保存之后，编码格式依然为 utf8