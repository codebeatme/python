
try:
    # 除数为 0 将引发异常 ZeroDivisionError
    num = 1 / 0
except Exception:
    # Exception 是 ZeroDivisionError 的基类，这里的代码会被执行
    print('匹配到了异常 ZeroDivisionError')
except ZeroDivisionError:
    print('无人问津！')

try:
    # 访问未定义的 undefined，将引发异常 NameError
    print(undefined)
except IOError:
    # IOError 不是 NameError 的基类，这里的代码不会执行
    print('出现了 IO 错误？不可能')