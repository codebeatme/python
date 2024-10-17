from datetime import time, datetime, timedelta, tzinfo

# 自定义时区 CustomDST
class CustomDST(tzinfo):
    # 返回日期时间在夏令时中的时间差值
    def dst(self, dt: datetime):

        # 当调用 time 对象的 dst 方法时，dt 为 None
        if not dt:
            # 这里应该返回 None 或 timedelta()，但我们尝试返回其他值
            return timedelta(minutes=15)

        # 时区 CustomDST 将 6，7，8 月份视为夏令时
        if dt.month >= 6 and dt.month <= 8:
            # 夏令时的时间差值为 1 小时
            return timedelta(hours=1)
        else:
            return timedelta()

cz = CustomDST()
# 6 月 1 日属于夏令时
print(cz.dst(datetime(2024, 6, 1)))
# 9 月 1 日不属于夏令时
print(datetime(2024, 9, 1, tzinfo=cz).dst())
# 时区 CustomDST 会为 time 对象返回 timedelta(minutes=15)
print(time().dst(), time(tzinfo=cz).dst())
