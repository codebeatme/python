def jump():
    try:
        raise BaseExceptionGroup('跳转', [NameError()])
    except* NameError:
        # ERROR 不能使用跳转语句
        return

jump()