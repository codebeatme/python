from datetime import time, datetime, timedelta, tzinfo

# 自訂時區 CustomDST
class CustomDST(tzinfo):
    # 傳回日期時間在夏令時中的時間差值
    def dst(self, dt: datetime):

        # 當呼叫 time 物件的 dst 方法時，dt 為 None
        if not dt:
            # 這裏應該傳回 None 或 timedelta()，但我們嘗試傳回其他值
            return timedelta(minutes=15)

        # 時區 CustomDST 將 6，7，8 月份視為夏令時
        if dt.month >= 6 and dt.month <= 8:
            # 夏令時的時間差值為 1 小時
            return timedelta(hours=1)
        else:
            return timedelta()

cz = CustomDST()
# 6 月 1 日屬於夏令時
print(cz.dst(datetime(2024, 6, 1)))
# 9 月 1 日不屬於夏令時
print(datetime(2024, 9, 1, tzinfo=cz).dst())
# 時區 CustomDST 會為 time 物件傳回 timedelta(minutes=15)
print(time().dst(), time(tzinfo=cz).dst())
