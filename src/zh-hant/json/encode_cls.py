import json
from datetime import date

# 自訂 JSON 編碼器 MyEncoder
class MyEncoder(json.JSONEncoder):
    # 建構函式需要保留 JSONEncoder 的關鍵字參數
    def __init__(self, date_template, **kwds) -> None:
        super().__init__(**kwds)
        super().__init__()

        self.date_template = date_template

    # 覆寫 default 方法，用來處理不能編碼的物件
    def default(self, o):

        # 如果是日期物件，則轉換為一個字串
        if (isinstance(o, date)):
            return self.date_template.format(o.year, o.month, o.day)

        return super().default(o)

# 建立編碼器並呼叫 encode 方法進行編碼
print(MyEncoder('{0}/{1}/{2}').encode(date(2024, 1, 1)))
# 使用 dumps 函式和編碼器 MyEncoder 進行編碼
print(json.dumps(
    [10, 'Tom', date(2024, 10, 10)],
    cls=MyEncoder,
    separators=(',', ':'),
    date_template='{0}-{1}-{2}')
)