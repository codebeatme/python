err = ExceptionGroup('异常组', [NameError()])
new_err = err.derive([ValueError()])

# 显示原有异常组和新异常组
print(f'{err.message} {err.exceptions}')
print(f'{new_err.message} {new_err.exceptions}')