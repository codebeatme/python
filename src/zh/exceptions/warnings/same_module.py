import warnings

# 指向同一模块的同类警告，仅显示一次
warnings.filterwarnings('module')

# 显示警告 A
def test():
    warnings.warn('警告 A', UserWarning)

# test 函数中的警告将被显示
test()
# 下面的警告不会被显示，因为他与 test 中的警告属于同一类
warnings.warn('警告 A', UserWarning)

# 显示警告 B
# 警告 B 将被显示，因为他与警告 A 不是同一类
warnings.warn('警告 B', UserWarning)
from datetime import date
today = date(2024, 11, 11)
# 下面的警告不会被显示，因为他与上一个警告 B 属于同一类
warnings.warn('警告 B', UserWarning, source=today)
# 下面的警告会被显示，因为他指向了另一个模块
warnings.warn('警告 B', UserWarning, stacklevel=2)
# 下面的警告不会被显示，因为他与上一个警告 B 属于同一类，并且指向了同一个模块
import os
warnings.warn('警告 B', UserWarning, skip_file_prefixes=(os.path.dirname(__file__),))
