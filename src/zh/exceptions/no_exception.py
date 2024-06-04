def no_exception(r):
    try:
        # 引发异常 AttributeError
        raise AttributeError()
    finally:
        if r:
            print('调用了 return 语句')
            # 这里的 return 语句将导致未处理的异常不被抛出
            return
        else:
            print('没有调用 return 语句')

# 不会显示错误信息
no_exception(True)
# 会显示错误信息
no_exception(False)