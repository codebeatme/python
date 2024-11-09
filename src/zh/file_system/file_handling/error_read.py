# 请将命令行跳转至脚本文件 error_read.py 所在的目录，然后运行他

# 函数 read 将打开文件并读取其中的内容
def read(e):
    try:
        file = open('error.txt', 'r', encoding='ascii', errors=e)
        # 显示文件中的内容
        text = file.read()
        print(f'{e} {text}')
    except Exception as err:
        print(f'{e} {err}')

# 使用不同的错误处理方式读取文件 error.txt
read('strict')
read('ignore')
read('replace')
read('backslashreplace')
# read('xmlcharrefreplace')
# read('namereplace')
# read('surrogateescape')
