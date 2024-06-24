# 将 Warning 类作为异常来使用
try:
    raise Warning
except Warning as err:
    print(type(err))