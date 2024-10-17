from datetime import datetime, timedelta, tzinfo, timezone

# 自訂時區 MyZone
class MyZone(tzinfo):
    # 時區 MyZone 與零時區之間的固定時間差值為 3 小時
    def utcoffset(self, dt):
        return timedelta(hours=3) + self.dst(dt)

    # 時區 MyZone 將 7 月份視為夏令時
    def dst(self, dt):
        if dt and dt.month == 7:
            return timedelta(hours=1)
        else:
            return timedelta()


# 建立 MyZone 時區
myz = MyZone()
# 將零時區的日期時間轉換為 MyZone 時區的日期時間
print(datetime(2024, 2, 1, tzinfo=timezone.utc).astimezone(myz))
# 將零時區的日期時間轉換為 MyZone 時區的夏令時日期時間
print(datetime(2024, 7, 1, tzinfo=timezone.utc).astimezone(myz))
# 將零時區的日期時間轉換本機日期時間（假設作業系統的時區為 UTC+8）
print(datetime(2024, 3, 1, tzinfo=timezone.utc).astimezone())
# 將本機日期時間（假設作業系統的時區為 UTC+8）轉換為 MyZone 時區的日期時間
print(datetime(2024, 5, 1).astimezone(MyZone()))

# 直接呼叫 fromutc 方法，效果等同於上面的第一個時區轉換
print(myz.fromutc(datetime(2024, 2, 1, tzinfo=myz)))
