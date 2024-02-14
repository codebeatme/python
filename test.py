
def is_numeric(obj, cls=None) -> bool:
    '''判断目标是否为数字类型，整数类型，浮点数类型或复数类型。

    :param obj 需要判断的目标。
    :param cls 可以是 int，float，complex 中的一个，或一个包含他们的元组，以判断是否为整数类型，浮点数类型或复数类型。默认值为 None，表示判断是否为任意数字类型。
    '''

    if not cls:
        from numbers import Number
        return isinstance(obj, Number)
    else:
        return isinstance(obj, cls)
