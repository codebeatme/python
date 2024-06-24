import warnings

# 将警告保存在 log 列表中
with warnings.catch_warnings(record=True) as log:
    warnings.warn('第一个警告', UserWarning)
    # 下面的警告不会被保存至 log，因为该警告本身会被忽略
    warnings.warn('第二个警告', ImportWarning)

# 显示 with 语句中发出的警告
for warning in log:
    print(f'{warning.message} {warning.lineno}')