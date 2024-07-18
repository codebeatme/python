import json
from io import StringIO

# 使用 load 函数解析存储在 StringIO 对象中的 JSON 字符串
s = StringIO('{"name": "Jack", "age": 10}')
print(json.load(s))

# 分别通过 str，bytes 对象提供 JSON 字符串
print(json.loads('{"id": "red", "color": "#ff0000"}'))
# 最后一个 height 才是有效的
print(json.loads(b'{"width": 100, "height": 200, "height": 300}'))

from json import JSONDecoder
import re

d = JSONDecoder()
# 将 +++ 或 --- 作为 JSON 的边界
print(d.decode('+++[1, 2, 3, "A", "B", "C"]---', re.compile(r'\+{3}|-{3}').match))
# 将第 4 个字符 { 作为 JSON 的开始
print(d.raw_decode('开始：{"name": "Jack"}，这里有个 JSON', 3))