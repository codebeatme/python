import warnings

# 忽略行號為 5 的型別為 UserWarning 的警告
warnings.simplefilter('ignore', UserWarning, 5)
warnings.warn('我被忽略了', UserWarning)

# 忽略行號為 11 的警告
warnings.simplefilter('ignore', lineno=11)
# 下面的規則將替代上面的規則生效
warnings.simplefilter('always', lineno=11)
warnings.warn('顯示')