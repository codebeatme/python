'這裏是模組 '"teacher"

# 模組 teacher 中的變數 count，level
count = 0
level = 1

# 模組 teacher 中的函式 show
def show():
    print(f'教師的數量為 {count}')

# 使用 _ 開頭，表示不適合外部存取
__avg_age = 33
def _add_avg_age(years):
    # 修改模組變數 __avg_age
    global __avg_age
    __avg_age += years