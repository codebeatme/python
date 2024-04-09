'这里是模块 '"teacher"

# 模块 teacher 中的变量 count，level
count = 0
level = 1

# 模块 teacher 中的函数 show
def show():
    print(f'教师的数量为 {count}')

# 使用 _ 开头，表示不适合外部访问
__avg_age = 33
def _add_avg_age(years):
    # 修改模块变量 __avg_age
    global __avg_age
    __avg_age += years