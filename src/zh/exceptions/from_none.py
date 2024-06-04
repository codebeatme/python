try:
    try:
        # 引发异常 ZeroDivisionError
        1 / 0
    except:
        # 引发异常 RuntimeError，但将原因设置为 None
        raise RuntimeError from None
except Exception as err:
    print(type(err.__context__))
    print(err.__cause__)
    print(err.__suppress_context__)
    # 重新抛出异常
    raise
