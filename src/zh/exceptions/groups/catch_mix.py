# ERROR 无法混合使用 except* 和 except
try:
    raise ExceptionGroup('混合使用', [SystemExit()])
except* SystemExit:
    pass
except:
    pass