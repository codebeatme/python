import warnings

# 指向同一模組的同類警告，僅顯示一次
warnings.filterwarnings('module')

# 顯示警告 A
def test():
    warnings.warn('警告 A', UserWarning)

# test 函式中的警告將被顯示
test()
# 下面的警告不會被顯示，因為他與 test 中的警告屬於同一類
warnings.warn('警告 A', UserWarning)

# 顯示警告 B
# 警告 B 將被顯示，因為他與警告 A 不是同一類
warnings.warn('警告 B', UserWarning)
from datetime import date
today = date(2024, 11, 11)
# 下面的警告不會被顯示，因為他與上一個警告 B 屬於同一類
warnings.warn('警告 B', UserWarning, source=today)
# 下面的警告會被顯示，因為他指向了另一個模組
warnings.warn('警告 B', UserWarning, stacklevel=2)
# 下面的警告不會被顯示，因為他與上一個警告 B 屬於同一類，並且指向了同一個模組
import os
warnings.warn('警告 B', UserWarning, skip_file_prefixes=(os.path.dirname(__file__),))
