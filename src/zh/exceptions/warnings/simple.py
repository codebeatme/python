import warnings

# 忽略行号为 5 的类型为 UserWarning 的警告
warnings.simplefilter('ignore', UserWarning, 5)
warnings.warn('我被忽略了', UserWarning)

# 忽略行号为 11 的警告
warnings.simplefilter('ignore', lineno=11)
# 下面的规则将替代上面的规则生效
warnings.simplefilter('always', lineno=11)
warnings.warn('显示')