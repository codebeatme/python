try:
    try:
        # 引发异常 ZeroDivisionError
        1 / 0
    except:
        # 处理 ZeroDivisionError 之后，引发新的异常 ValueError
        raise ValueError
except Exception as err:
    # 显示异常的 __context__ 变量的类型
    print(f'{type(err)} 的 __context__ 的类型为 {type(err.__context__)}')

try:
    try:
        # 引发异常 ZeroDivisionError
        1 / 0
    except:
        # 引发异常 RuntimeError，但并未将 ZeroDivisionError 作为原因
        raise RuntimeError from ValueError
except Exception as err:
    print(type(err.__context__))
    print(type(err.__cause__))
    print(err.__suppress_context__)
    err.__suppress_context__ = False
    # 重新抛出异常
    raise
