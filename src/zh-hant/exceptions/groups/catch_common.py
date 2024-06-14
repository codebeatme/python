# 擷取普通的例外狀況
try:
    raise NameError()
except* NameError as err:
    # NameError 被轉換為例外狀況群組
    print(f'{type(err)} 訊息：“{err.message}”，例外狀況：{err.exceptions}')