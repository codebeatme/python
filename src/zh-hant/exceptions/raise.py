try:
    # 擲回例外狀況 NameError
    raise NameError
except NameError:
    # 在比對例外狀況之後，重新將其擲回
    raise
