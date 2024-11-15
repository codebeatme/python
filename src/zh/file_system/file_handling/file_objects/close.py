# 请将命令行跳转至脚本文件 close.py 所在的目录，然后运行他
file = open('close.txt', 'w', encoding='utf8')
file.write('写入一些数据！')
# 关闭文件
file.close()

# ERROR 文件已经关闭
file.write('再写入一些数据？')