# 在异常组中包含异常组，并使用异常 BaseException
BaseExceptionGroup(
    '异常组 BaseExceptionGroup',
    [BaseExceptionGroup('包含在异常组中的异常组', [BaseException()])]
)

# 在异常组 ExceptionGroup 中使用异常 BaseException
ExceptionGroup(
    '异常组 ExceptionGroup',
    # ERROR 不能包含 BaseException
    [Exception(), BaseException()]
)
