# 將 Warning 類別作為例外狀況來使用
try:
    raise Warning
except Warning as err:
    print(type(err))