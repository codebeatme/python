try:
    # 抛出异常 ValueError
    raise ValueError
except ValueError:
    # 抛出新的异常 NameError，该异常无法被处理
    raise NameError
finally:
    print('执行 finally 中的代码后，才能看到错误信息')