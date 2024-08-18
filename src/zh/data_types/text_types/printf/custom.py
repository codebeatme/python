# 一个用于格式化的类
class Data:
    # 定义了 __bytes__ 方法
    def __bytes__(self):
        return bytes(b'__bytes__')

print(b'%b' % Data())