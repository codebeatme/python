# SystemExit 直接繼承自 BaseException
err = BaseExceptionGroup('例外狀況群組 BaseExceptionGroup', (SystemExit(),))
print(type(err))

# NameError 直接繼承自 Exception
err = BaseExceptionGroup('例外狀況群組 ExceptionGroup', (NameError(),))
print(type(err))