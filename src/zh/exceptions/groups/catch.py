# 将 Python 异常组作为一个整体进行捕获
try:
    raise ExceptionGroup('毫无意义', (IOError(),))
except BaseExceptionGroup as err:
    print(f'捕获的异常类型为：{type(err)}')

try:
    raise BaseExceptionGroup('捕获', [NameError(), ValueError(), BaseException()])
except* (NameError, ValueError) as err:
    # 转换的异常组的类型为 ExceptionGroup
    print(f'异常类型为：{type(err)}，{err.message} {err.exceptions}')
except* BaseException:
    # 转换的异常组的类型为 BaseExceptionGroup
    import sys
    # 通过 exception 函数获取转换的异常组
    err = sys.exception()
    print(f'异常类型为：{type(err)}，{err.message} {err.exceptions}')

try:
    raise BaseExceptionGroup('匹配多个异常', [Exception(), Exception(), IOError(), IOError(), FileNotFoundError()])
except* IOError as err:
    # 匹配 IOError，FileNotFoundError
    print(err.exceptions)
except* Exception as err:
    # 只能匹配到 Exception
    print(err.exceptions)