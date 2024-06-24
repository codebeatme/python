import warnings

# 將警告儲存在 log 串列中
with warnings.catch_warnings(record=True) as log:
    warnings.warn('第一個警告', UserWarning)
    # 下面的警告不會被儲存至 log，因為該警告本身會被忽略
    warnings.warn('第二個警告', ImportWarning)

# 顯示 with 陳述式中發出的警告
for warning in log:
    print(f'{warning.message} {warning.lineno}')