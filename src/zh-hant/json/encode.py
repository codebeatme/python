import json
from io import StringIO
from datetime import date

# 使用 StringIO 物件儲存 JSON 字串
s = StringIO()
json.dump(
    {'name': '你好，Jack', 'age': 10, date(2024, 7, 17): True}, s,
    # 第三個鍵值組將被忽略
    skipkeys=True,
    # 不逸出非 ASCII 字元
    ensure_ascii=False
)
print(s.getvalue())

# dumps 函式直接傳回 JSON 字串
s = json.dumps(
    [
        {'name': 'Tom', 'age': 10},
        {'name': 'Harry', 'age': 11}
    ],
    # 使用一個空格進行縮排
    indent=1,
    # 使用 ; 分隔鍵值組或元素，使用 = 分隔鍵和值
    separators=(';', '='),
    # 對鍵值組進行排序
    sort_keys=True
)
print(s)

# ERROR 表示負無限大的浮點數無法被傾印
json.dumps(float('-inf'), allow_nan=False)