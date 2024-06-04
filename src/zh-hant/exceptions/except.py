import random
import sys

try:
    # 從多個例外狀況中隨機選擇一個並引發
    errs = [TypeError, AttributeError, ZeroDivisionError, IndexError]
    err = errs[random.randint(0, 3)]
    raise err()
except (TypeError, AttributeError) as e:
    # 檢視例外狀況的具體型別
    print(f'例外狀況 {type(e)}')
except:
    # 既不是 TypeError 也不是 AttributeError 的例外狀況
    print(f'其他例外狀況 {type(sys.exception())}')

