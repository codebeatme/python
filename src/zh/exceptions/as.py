import sys
# 该变量稍后会被删除
err = 'error'

try:
    # 除数为 0 将引发异常 ZeroDivisionError
    1 / 0
except ZeroDivisionError as err:
    # 通过标识符 err 和 exception 函数获取的异常对象相同
    print(sys.exception() == err)

print(sys.exception())
print(err)
