import json
import math

# 一个继承自 JSONDecoder 的类
class MyDecoder(json.JSONDecoder):
    def __init__(self, strict):
        super().__init__(
            # 指定处理 JSON 数字的函数或方法
            parse_float=lambda v: math.ceil(float(v)),
            parse_int=MyDecoder.convert_int,
            strict=strict
        )

        # 直接修改变量 parse_int 不会产生任何效果
        self.parse_int = lambda v: int(v) + 1000

    # 用于处理整数的方法 convert_int
    @staticmethod
    def convert_int(value):
        i = int(value)
        return 0 if i < 0 else i

# 使用类 MyDecoder 完成 JSON 字符串的解析
o = json.loads(
    '[-100, 1.2, "\t一个制表符"]',
    cls=MyDecoder,
    # 参数 strict 将在创建 MyDecoder 对象时被使用
    strict=False
)
print(o)
