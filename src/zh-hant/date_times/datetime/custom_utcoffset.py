from datetime import time, datetime, timedelta, tzinfo

# 自訂時區 CustomUTCOffset
class CustomUTCOffset(tzinfo):
    # 初始化自訂時區
    def __init__(self, hours):
        self.hours = timedelta(hours=hours)

    # 計算日期時間與零時區之間的時間差值
    def utcoffset(self, dt):
        # 需要判斷是否為 None，因為 dst 方法可能傳回 None
        dst = self.dst(dt)
        return self.hours + (timedelta(0) if dst is None else dst)
    
    # 全年處於夏令時
    def dst(self, dt):
        return timedelta(hours=1) if dt else None

# 與零時區相差 5 個小時
cz = CustomUTCOffset(5)
# 時區 CustomUTCOffset 為 datetime 物件傳回的夏令時時間差值為 1 小時
print(cz.utcoffset(datetime(2024, 9, 1)))
# 時區 CustomUTCOffset 為 time 物件傳回的夏令時時間差值為 None
print(time().utcoffset(), time(tzinfo=cz).utcoffset())
