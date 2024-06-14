try:
    raise BaseExceptionGroup('异常组', [
        ExceptionGroup('子异常组', [ValueError(), NameError()])
    ])
# ERROR 不能匹配 ExceptionGroup
except* ExceptionGroup:
    pass