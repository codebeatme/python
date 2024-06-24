import warnings
# 正常情況下，下面的警告不會顯示
warnings.warn('警告', ImportWarning)
# 正常情況下，下面的警告不會作為例外狀況被擲回
warnings.warn('Err 擲回例外狀況')