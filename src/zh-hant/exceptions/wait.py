try:
    # 擲回例外狀況 ValueError
    raise ValueError
except ValueError:
    # 擲回新的例外狀況 NameError，該例外狀況無法被處理
    raise NameError
finally:
    print('執行 finally 中的程式碼後，才能看到錯誤資訊')