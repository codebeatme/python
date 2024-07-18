import json

# 循环引用字典对象
o = dict()
o['self'] = o

try:
    # 检测对象是否存在循环引用
    json.dumps(o, check_circular=True)
except Exception as err:
    print(err)

try:
    # 不检测对象是否存在循环引用，但依然会导致异常
    json.dumps(o, check_circular=False)
except Exception as err:
    print(err)