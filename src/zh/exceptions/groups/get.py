err = ExceptionGroup('获取异常', (
    NameError(), ValueError(),
    BaseExceptionGroup('子异常组', [OSError(), NameError()])
))

# 返回 None
print(err.subgroup(AttributeError))
# 获取异常组中的 NameError 和 ValueError
group = err.subgroup((NameError, ValueError))
print(f'{group.message} {group.exceptions}')

# 判断异常是否符合条件的函数 get_error
def get_error(err):
    return type(err) in (NameError, ValueError)

# 通过函数获取异常组中的 NameError 和 ValueError，以及剩余异常
m, r = err.split(get_error)
print(f'{m.message} {m.exceptions} {r.message} {r.exceptions}')
