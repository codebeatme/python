# 请将命令行跳转至脚本文件 closed.py 所在的目录，然后运行他
# with 语句结束之后，文件将被关闭
with open('close.txt', 'w', encoding='utf8') as file:
    file.write('写入一些数据！')

# 检查文件是否被关闭
if file.closed:
    print('文件 close.txt 已经关闭')