from datetime import datetime, timedelta, tzinfo, timezone

# 自定义时区 MyZone
class MyZone(tzinfo):
    # 时区 MyZone 与零时区之间的固定时间差值为 3 小时
    def utcoffset(self, dt):
        return timedelta(hours=3) + self.dst(dt)

    # 时区 MyZone 将 7 月份视为夏令时
    def dst(self, dt):
        if dt and dt.month == 7:
            return timedelta(hours=1)
        else:
            return timedelta()


# 创建 MyZone 时区
myz = MyZone()
# 将零时区的日期时间转换为 MyZone 时区的日期时间
print(datetime(2024, 2, 1, tzinfo=timezone.utc).astimezone(myz))
# 将零时区的日期时间转换为 MyZone 时区的夏令时日期时间
print(datetime(2024, 7, 1, tzinfo=timezone.utc).astimezone(myz))
# 将零时区的日期时间转换本地日期时间（假设操作系统的时区为 UTC+8）
print(datetime(2024, 3, 1, tzinfo=timezone.utc).astimezone())
# 将本地日期时间（假设操作系统的时区为 UTC+8）转换为 MyZone 时区的日期时间
print(datetime(2024, 5, 1).astimezone(MyZone()))

# 直接调用 fromutc 方法，效果等同于上面的第一个时区转换
print(myz.fromutc(datetime(2024, 2, 1, tzinfo=myz)))
