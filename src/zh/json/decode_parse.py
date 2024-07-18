import json

# 一些处理 JSON 数字的函数
def convert_float(value):
    # 将浮点数四舍五入
    return round(float(value))

def convert_int(value):
    # 将整数转换为 Yes 或 No
    i = int(value)
    return 'No' if i < 0 else 'Yes'

def convert_constant(value):
    # 将 NaN，Infinity，-Infinity 转换为 None
    return None

# NaN，Infinity 将被转换为 None
o = json.loads(
    '[1.2, 1.5, -1, 1, NaN, Infinity, "-Infinity", null, true, false]',
    parse_float=convert_float,
    parse_int=convert_int,
    parse_constant=convert_constant
)
print(f'parse {o}')

# NaN，Infinity，-Infinity 会转换为 float 类型
o = json.loads('[NaN, Infinity, -Infinity]')
for n in o:
    print(f'{type(n)} {n}')