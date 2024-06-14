def jump():
    try:
        raise BaseExceptionGroup('跳躍', [NameError()])
    except* NameError:
        # ERROR 不能使用跳躍陳述式
        return

jump()