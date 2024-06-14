# 抛出包含异常 ValueError 和 NameError 的异常组
raise ExceptionGroup('糟糕，又错了', (ValueError(), NameError()))
