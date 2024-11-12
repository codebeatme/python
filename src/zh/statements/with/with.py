# 文件对象的 __enter__ 方法返回自身
with open('with.txt', 'w', encoding='utf8') as file:
    file.write('with 语句')

# ERROR 文件对象已经被关闭
file.write('又一条 with 语句')
file.__exit__