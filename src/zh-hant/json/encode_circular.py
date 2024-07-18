import json

# 迴圈參考字典物件
o = dict()
o['self'] = o

try:
    # 檢測物件是否存在迴圈參考
    json.dumps(o, check_circular=True)
except Exception as err:
    print(err)

try:
    # 不檢測物件是否存在迴圈參考，但依然會導致例外狀況
    json.dumps(o, check_circular=False)
except Exception as err:
    print(err)