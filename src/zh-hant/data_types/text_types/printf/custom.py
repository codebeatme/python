# 一個用於格式化的類別
class Data:
    # 定義了 __bytes__ 方法
    def __bytes__(self):
        return bytes(b'__bytes__')

print(b'%b' % Data())