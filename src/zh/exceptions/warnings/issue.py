import warnings
from datetime import date

# 检查日期的函数
def check(today):
    # 如果是 11 月 11 日，则发出警告
    if today.month == 11 and today.day == 11:
        # 警告将指向 check 的调用者，并显示 today 的回溯信息
        warnings.warn('11 月 11 日？', Warning, 2, today)

goodday = date(2024, 11, 11)
check(goodday)
