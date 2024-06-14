err = ExceptionGroup('取得例外狀況', (
    NameError(), ValueError(),
    BaseExceptionGroup('子例外狀況群組', [OSError(), NameError()])
))

# 傳回 None
print(err.subgroup(AttributeError))
# 取得例外狀況群組中的 NameError 和 ValueError
group = err.subgroup((NameError, ValueError))
print(f'{group.message} {group.exceptions}')

# 判斷例外狀況是否符合條件的函式 get_error
def get_error(err):
    return type(err) in (NameError, ValueError)

# 通過函式取得例外狀況群組中的 NameError 和 ValueError，以及剩余例外狀況
m, r = err.split(get_error)
print(f'{m.message} {m.exceptions} {r.message} {r.exceptions}')
