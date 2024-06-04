def show():
    try:
        # 返回之前会执行 finally 中的代码
        return '一条消息'
    finally:
        # 在真正返回之前，这里的代码将被执行
        print(f'在返回之前执行！')


print(show())


def div(a, b):
    try:
        # 如果除数为 0，则引发异常 ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        # 这里的返回值将被忽略
        return 0
    finally:
        # 这里是最终的返回值
        return a / (b + 1)

print(div(2, 0))
