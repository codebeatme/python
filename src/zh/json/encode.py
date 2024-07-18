import json
from io import StringIO
from datetime import date

# 使用 StringIO 对象存储 JSON 字符串
s = StringIO()
json.dump(
    {'name': '你好，Jack', 'age': 10, date(2024, 7, 17): True}, s,
    # 第三个键值对将被忽略
    skipkeys=True,
    # 不转义非 ASCII 字符
    ensure_ascii=False
)
print(s.getvalue())

# dumps 函数直接返回 JSON 字符串
s = json.dumps(
    [
        {'name': 'Tom', 'age': 10},
        {'name': 'Harry', 'age': 11}
    ],
    # 使用一个空格进行缩进
    indent=1,
    # 使用 ; 分隔键值对或元素，使用 = 分隔键和值
    separators=(';', '='),
    # 对键值对进行排序
    sort_keys=True
)
print(s)

# ERROR 表示负无穷的浮点数无法被转储
json.dumps(float('-inf'), allow_nan=False)