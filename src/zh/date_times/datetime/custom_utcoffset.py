from datetime import time, datetime, timedelta, tzinfo

# 自定义时区 CustomUTCOffset
class CustomUTCOffset(tzinfo):
    # 初始化自定义时区
    def __init__(self, hours):
        self.hours = timedelta(hours=hours)

    # 计算日期时间与零时区之间的时间差值
    def utcoffset(self, dt):
        # 需要判断是否为 None，因为 dst 方法可能返回 None
        dst = self.dst(dt)
        return self.hours + (timedelta(0) if dst is None else dst)
    
    # 全年处于夏令时
    def dst(self, dt):
        return timedelta(hours=1) if dt else None

# 与零时区相差 5 个小时
cz = CustomUTCOffset(5)
# 时区 CustomUTCOffset 为 datetime 对象返回的夏令时时间差值为 1 小时
print(cz.utcoffset(datetime(2024, 9, 1)))
# 时区 CustomUTCOffset 为 time 对象返回的夏令时时间差值为 None
print(time().utcoffset(), time(tzinfo=cz).utcoffset())
