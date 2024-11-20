# 请将命令行跳转至脚本文件 error_write.py 所在的目录，然后运行他

# 函数 write 将打开文件并写入一些内容
def write(e):
    try:
        file = open(f'error_{e}.txt', 'w', encoding='ascii', errors=e)
        # 将内容写入文件
        file.write('今天 is good')
    except Exception as err:
        print(f'{e} {err}')


# 使用不同的错误处理方式写入文件
write('strict')
write('ignore')
write('replace')
write('backslashreplace')
write('xmlcharrefreplace')
write('namereplace')

# 查看文件中被写入的内容
for i in ('strict', 'ignore', 'replace', 'backslashreplace', 'xmlcharrefreplace', 'namereplace'):
    fn = f'error_{i}.txt'
    file = open(fn, 'r', encoding='ascii')
    print(f'{fn} {file.read()}')
