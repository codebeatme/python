# 捕获普通的异常
try:
    raise NameError()
except* NameError as err:
    # NameError 被转换为异常组
    print(f'{type(err)} 消息：“{err.message}”，异常：{err.exceptions}')