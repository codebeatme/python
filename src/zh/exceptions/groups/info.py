try:
    # 由于所包含的异常均继承自 Exception，因此会得到一个 ExceptionGroup 对象
    raise BaseExceptionGroup(
        '这仅仅是一个测试！',
        [NameError(), ValueError()]
    )
except ExceptionGroup as err:
    # 显示异常组的相关内容
    print(f'来自异常组的信息：{err.message}')
    print(f'异常组中的异常：{err.exceptions}')
