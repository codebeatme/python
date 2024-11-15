# 请将命令行跳转至脚本文件 truncate.py 所在的目录，然后运行他
with open('truncate.txt', 'r+', encoding="utf8") as file:
    # 显示文件内容
    print(file.read())
    # 保留“真是美好”
    print(f'从第 12 个字节处截断：{file.truncate(12)}')
    # 文件指针位置不会被 truncate 方法改变
    print(f'当前指针位置：{file.tell()}')