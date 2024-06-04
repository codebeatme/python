try:
    try:
        # 引發例外狀況 ZeroDivisionError
        1 / 0
    except:
        # 處理 ZeroDivisionError 之後，引發新的例外狀況 ValueError
        raise ValueError
except Exception as err:
    # 顯示例外狀況的 __context__ 變數的型別
    print(f'{type(err)} 的 __context__ 的型別為 {type(err.__context__)}')

try:
    try:
        # 引發例外狀況 ZeroDivisionError
        1 / 0
    except:
        # 引發例外狀況 RuntimeError，但並未將 ZeroDivisionError 作為原因
        raise RuntimeError from ValueError
except Exception as err:
    print(type(err.__context__))
    print(type(err.__cause__))
    print(err.__suppress_context__)
    err.__suppress_context__ = False
    # 重新擲回例外狀況
    raise
