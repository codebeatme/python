import random
import sys

try:
    # 从多个异常中随机选择一个并引发
    errs = [TypeError, AttributeError, ZeroDivisionError, IndexError]
    err = errs[random.randint(0, 3)]
    raise err()
except (TypeError, AttributeError) as e:
    # 查看异常的具体类型
    print(f'异常 {type(e)}')
except:
    # 既不是 TypeError 也不是 AttributeError 的异常
    print(f'其他异常 {type(sys.exception())}')

