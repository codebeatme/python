try:
    try:
        # 引發例外狀況 ZeroDivisionError
        1 / 0
    except:
        # 引發例外狀況 RuntimeError，但將原因設定為 None
        raise RuntimeError from None
except Exception as err:
    print(type(err.__context__))
    print(err.__cause__)
    print(err.__suppress_context__)
    # 重新擲回例外狀況
    raise
