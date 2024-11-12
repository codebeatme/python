# 请将命令行跳转至脚本文件 mode.py 所在的目录，然后运行他
# 可以对文件进行读写，若文件不存在则引发异常
file = open('info.txt', 'r+', encoding='utf8')

# 读取文件中的行
print(file.readlines())
# 写入新的行
file.writelines(['\n这是新的一行'])

# 需要 r，w，a，x 中的一个
try: open('info.txt', 't', encoding='utf8')
except ValueError as e: print(e)
# r，w，a，x 不能同时出现
try: open('info.txt', 'rw', encoding='utf8')
except ValueError as e: print(e)