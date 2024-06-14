try:
    raise BaseExceptionGroup('例外狀況群組', [
        ExceptionGroup('子例外狀況群組', [ValueError(), NameError()])
    ])
# ERROR 不能比對 ExceptionGroup
except* ExceptionGroup:
    pass