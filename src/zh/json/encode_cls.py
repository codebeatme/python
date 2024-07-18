import json
from datetime import date

# 自定义 JSON 编码器 MyEncoder
class MyEncoder(json.JSONEncoder):
    # 构造函数需要保留 JSONEncoder 的关键字参数
    def __init__(self, date_template, **kwds) -> None:
        super().__init__(**kwds)
        super().__init__()

        self.date_template = date_template

    # 重写 default 方法，用来处理不能编码的对象
    def default(self, o):

        # 如果是日期对象，则转换为一个字符串
        if (isinstance(o, date)):
            return self.date_template.format(o.year, o.month, o.day)

        return super().default(o)

# 创建编码器并调用 encode 方法进行编码
print(MyEncoder('{0}/{1}/{2}').encode(date(2024, 1, 1)))
# 使用 dumps 函数和编码器 MyEncoder 进行编码
print(json.dumps(
    [10, 'Tom', date(2024, 10, 10)],
    cls=MyEncoder,
    separators=(',', ':'),
    date_template='{0}-{1}-{2}')
)