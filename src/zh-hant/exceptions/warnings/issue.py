import warnings
from datetime import date

# 檢查日期的函式
def check(today):
    # 如果是 11 月 11 日，則發出警告
    if today.month == 11 and today.day == 11:
        # 警告將指向 check 的呼叫者，並顯示 today 的回溯資訊
        warnings.warn('11 月 11 日？', Warning, 2, today)

goodday = date(2024, 11, 11)
check(goodday)
