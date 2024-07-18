import json

# 一些處理 JSON 數值的函式
def convert_float(value):
    # 將浮點數四舍五入
    return round(float(value))

def convert_int(value):
    # 將整數轉換為 Yes 或 No
    i = int(value)
    return 'No' if i < 0 else 'Yes'

def convert_constant(value):
    # 將 NaN，Infinity，-Infinity 轉換為 None
    return None

# NaN，Infinity 將被轉換為 None
o = json.loads(
    '[1.2, 1.5, -1, 1, NaN, Infinity, "-Infinity", null, true, false]',
    parse_float=convert_float,
    parse_int=convert_int,
    parse_constant=convert_constant
)
print(f'parse {o}')

# NaN，Infinity，-Infinity 會轉換為 float 型別
o = json.loads('[NaN, Infinity, -Infinity]')
for n in o:
    print(f'{type(n)} {n}')