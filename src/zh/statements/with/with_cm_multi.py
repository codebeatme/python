# 自定义 with 语句上下文管理器 CM
class CM:
    # CM 的构造器
    def __init__(self, name):
        self.name = name

    # __enter__ 和 __exit__ 方法将显示 CM 的名称
    def __enter__(self):
        print(f'__enter__ {self.name}')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'__exit__ {self.name} {exc_type}')


# 包含了两个上下文管理器
with (
    CM('A'),
    CM('B')
):
    pass

# 异常将按照 B，A 的顺序传播
with CM('A'), CM('B'):
    num = 1 / 0
