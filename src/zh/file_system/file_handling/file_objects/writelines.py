# 请将命令行跳转至脚本文件 writelines.py 所在的目录，然后运行他
# 将多个行写入文件
with open('writelines.txt', 'w', encoding='utf8') as file:
    file.writelines(('第一行\n', '第二行'))

# 将多个行写入文件
with open('writelinesb.txt', 'wb') as file:
    file.writelines(('第一行\n'.encode(), '第二行'.encode()))
