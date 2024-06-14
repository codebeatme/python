# 在例外狀況群組中包含例外狀況群組，並使用例外狀況 BaseException
BaseExceptionGroup(
    '例外狀況群組 BaseExceptionGroup',
    [BaseExceptionGroup('包含在例外狀況群組中的例外狀況群組', [BaseException()])]
)

# 在例外狀況群組 ExceptionGroup 中使用例外狀況 BaseException
ExceptionGroup(
    '例外狀況群組 ExceptionGroup',
    # ERROR 不能包含 BaseException
    [Exception(), BaseException()]
)
