err = ExceptionGroup('例外狀況群組', [NameError()])
new_err = err.derive([ValueError()])

# 顯示原有例外狀況群組和新例外狀況群組
print(f'{err.message} {err.exceptions}')
print(f'{new_err.message} {new_err.exceptions}')