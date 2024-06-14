# SystemExit 直接继承自 BaseException
err = BaseExceptionGroup('异常组 BaseExceptionGroup', (SystemExit(),))
print(type(err))

# NameError 直接继承自 Exception
err = BaseExceptionGroup('异常组 ExceptionGroup', (NameError(),))
print(type(err))