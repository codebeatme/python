try:
    # 例外狀況 NameError，OSError 會被重新擲回
    try:
        raise BaseExceptionGroup(
            '重新擲回', (
                NameError(), ValueError(),
                BaseExceptionGroup('巢狀的例外狀況', [OSError(), ValueError()])
            ))
    except* ValueError:
        # 兩個 ValueError 都會被擷取
        pass
except BaseExceptionGroup as err:
    # 例外狀況群組包含了 NameError 和巢狀的 OSError
    print(f'被重新擲回的例外狀況：{type(err)} {err.exceptions}')
