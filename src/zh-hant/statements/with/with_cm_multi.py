# 自訂 with 陳述式內容管理器 CM
class CM:
    # CM 的建構子
    def __init__(self, name):
        self.name = name

    # __enter__ 和 __exit__ 方法將顯示 CM 的名稱
    def __enter__(self):
        print(f'__enter__ {self.name}')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'__exit__ {self.name} {exc_type}')


# 包含了兩個內容管理器
with (
    CM('A'),
    CM('B')
):
    pass

# 例外狀況將按照 B，A 的順序傳播
with CM('A'), CM('B'):
    num = 1 / 0
