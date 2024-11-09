# 请将命令行跳转至脚本文件 file_exists.py 所在的目录，然后运行他
# 使用 r 模式打开不存在的文件 no.md
try: open('no.md', 'r')
except FileNotFoundError as e: print(e)

# 使用 a 模式将自动创建不存在的文件 no.md
open('no.md', 'a')

# 使用 x 模式打开已经存在的文件 no.md
try: open('no.md', 'x')
except FileExistsError as e: print(e)