# 將 Python 例外狀況群組作為一個整體進行擷取
try:
    raise ExceptionGroup('毫無意義', (IOError(),))
except BaseExceptionGroup as err:
    print(f'擷取的例外狀況型別為：{type(err)}')

try:
    raise BaseExceptionGroup('擷取', [NameError(), ValueError(), BaseException()])
except* (NameError, ValueError) as err:
    # 轉換的例外狀況群組的型別為 ExceptionGroup
    print(f'例外狀況型別為：{type(err)}，{err.message} {err.exceptions}')
except* BaseException:
    # 轉換的例外狀況群組的型別為 BaseExceptionGroup
    import sys
    # 通過 exception 函式取得轉換的例外狀況群組
    err = sys.exception()
    print(f'例外狀況型別為：{type(err)}，{err.message} {err.exceptions}')

try:
    raise BaseExceptionGroup('比對多個例外狀況', [Exception(), Exception(), IOError(), IOError(), FileNotFoundError()])
except* IOError as err:
    # 比對 IOError，FileNotFoundError
    print(err.exceptions)
except* Exception as err:
    # 只能比對到 Exception
    print(err.exceptions)