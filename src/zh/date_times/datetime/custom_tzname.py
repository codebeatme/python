from datetime import time, datetime, tzinfo

# 自定义时区 CustomTZName
class CustomTZName(tzinfo):
    # 初始化自定义时区
    def __init__(self, name):
        self.name = name

    # 返回时区名称
    def tzname(self, dt):

        if not dt:
            # 如果是 time 对象，则返回 TIME 作为时区名称
            return 'TIME'
        elif dt.month < 6 or dt.month > 8:
            # 如果不是夏令时，则返回创建 CustomTZName 对象时指定的时区名称
            return self.name
        else:
            # 如果是夏令时，则追加后缀 DST
            return self.name + ' DST'

# 时区名称为 My Zone
cz = CustomTZName('My Zone')
# 时区 CustomTZName 为 datetime 对象返回的非夏令时时区名称为 My Zone
print(cz.tzname(datetime(2024, 9, 1)))
# 时区 CustomTZName 为 datetime 对象返回的夏令时时区名称为 My Zone DST
print(cz.tzname(datetime(2024, 7, 1)))
# 时区 CustomTZName 为 time 对象返回的时区名称为 TIME
print(time().tzname(), time(tzinfo=cz).tzname())
