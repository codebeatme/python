# 自定义 with 语句上下文管理器 CM
class CM:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(exc_type, exc_value, exc_tb)
        raise exc_value

with CM():
    # 异常 ZeroDivisionError 被引发并且没有得到处理
    num = 1 / 0