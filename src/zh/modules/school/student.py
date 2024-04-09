# 以相对路径导入 teacher 模块的特性
from .teacher import *

print('在 student 模块中调用 show')
show()

# 以相对路径导入 guard 模块
from . import guard
print(f'守卫人员是 {guard.name}')