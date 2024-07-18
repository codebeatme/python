import json
import math

# 一個繼承自 JSONDecoder 的類別
class MyDecoder(json.JSONDecoder):
    def __init__(self, strict):
        super().__init__(
            # 指定處理 JSON 數值的函式或方法
            parse_float=lambda v: math.ceil(float(v)),
            parse_int=MyDecoder.convert_int,
            strict=strict
        )

        # 直接修改變數 parse_int 不會產生任何效果
        self.parse_int = lambda v: int(v) + 1000

    # 用於處理整數的方法 convert_int
    @staticmethod
    def convert_int(value):
        i = int(value)
        return 0 if i < 0 else i

# 使用類別 MyDecoder 完成 JSON 字串的解析
o = json.loads(
    '[-100, 1.2, "\t一個定位字元"]',
    cls=MyDecoder,
    # 參數 strict 將在建立 MyDecoder 物件時被使用
    strict=False
)
print(o)
