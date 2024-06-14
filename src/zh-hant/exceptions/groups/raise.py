# 擲回包含例外狀況 ValueError 和 NameError 的例外狀況群組
raise ExceptionGroup('糟糕，又錯了', (ValueError(), NameError()))
