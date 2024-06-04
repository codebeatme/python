try:
    # 抛出异常 NameError
    raise NameError
except NameError:
    # 在匹配异常之后，重新将其抛出
    raise
