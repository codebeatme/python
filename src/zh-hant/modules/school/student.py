# 以相對路徑匯入 teacher 模組的特性
from .teacher import *

print('在 student 模組中呼叫 show')
show()

# 以相對路徑匯入 guard 模組
from . import guard
print(f'守衛人員是 {guard.name}')