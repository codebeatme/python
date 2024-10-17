from datetime import time, datetime, tzinfo

# 自訂時區 CustomTZName
class CustomTZName(tzinfo):
    # 初始化自訂時區
    def __init__(self, name):
        self.name = name

    # 傳回時區名稱
    def tzname(self, dt):

        if not dt:
            # 如果是 time 物件，則傳回 TIME 作為時區名稱
            return 'TIME'
        elif dt.month < 6 or dt.month > 8:
            # 如果不是夏令時，則傳回建立 CustomTZName 物件時指定的時區名稱
            return self.name
        else:
            # 如果是夏令時，則追加尾碼 DST
            return self.name + ' DST'

# 時區名稱為 My Zone
cz = CustomTZName('My Zone')
# 時區 CustomTZName 為 datetime 物件傳回的非夏令時時區名稱為 My Zone
print(cz.tzname(datetime(2024, 9, 1)))
# 時區 CustomTZName 為 datetime 物件傳回的夏令時時區名稱為 My Zone DST
print(cz.tzname(datetime(2024, 7, 1)))
# 時區 CustomTZName 為 time 物件傳回的時區名稱為 TIME
print(time().tzname(), time(tzinfo=cz).tzname())
