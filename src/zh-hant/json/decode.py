import json
from io import StringIO

# 使用 load 函式解析儲存在 StringIO 物件中的 JSON 字串
s = StringIO('{"name": "Jack", "age": 10}')
print(json.load(s))

# 分別通過 str，bytes 物件提供 JSON 字串
print(json.loads('{"id": "red", "color": "#ff0000"}'))
# 最後一個 height 才是有效的
print(json.loads(b'{"width": 100, "height": 200, "height": 300}'))

from json import JSONDecoder
import re

d = JSONDecoder()
# 將 +++ 或 --- 作為 JSON 的邊界
print(d.decode('+++[1, 2, 3, "A", "B", "C"]---', re.compile(r'\+{3}|-{3}').match))
# 將第 4 個字元 { 作為 JSON 的開始
print(d.raw_decode('開始：{"name": "Jack"}，這裏有個 JSON', 3))