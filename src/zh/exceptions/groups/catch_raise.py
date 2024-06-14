try:
    # 异常 NameError，OSError 会被重新抛出
    try:
        raise BaseExceptionGroup(
            '重新抛出', (
                NameError(), ValueError(),
                BaseExceptionGroup('嵌套的异常', [OSError(), ValueError()])
            ))
    except* ValueError:
        # 两个 ValueError 都会被捕获
        pass
except BaseExceptionGroup as err:
    # 异常组包含了 NameError 和嵌套的 OSError
    print(f'被重新抛出的异常：{type(err)} {err.exceptions}')
