# 定义一个具有参数 name 的函数 hello
def hello(name):
    '''一个超级简单的函数'''
    print(f'你好，{name}')

# 调用函数 hello
hello('Kitty')

# 定义加法函数
def add(x=1, y=[], /, *, z):
    # 列表 y 添加数字 100
    y.append(100)
    print(y)

    # 计算 x，y，z 含有的数字之和
    num = 0
    for i in y:
        num += i

    return x + num + z

# z 只能作为关键字参数使用
print(add(z=1))
# x 作为位置参数被使用
print(add(1, z=3))

# 定了乘法函数
def mlp(*nums, **info):
    # 显示关键字参数
    print(info)

    # 计算 nums 中包含的位置参数
    num = 1
    for i in nums:
        num *= i

    return num

# 传递了多个数字进行乘法计算
print(mlp(2, 3, 4, 5, tip='这里是一个小小的提示'))

# 该函数将被之后定义的 wait 覆盖
def wait(seconds):
    print(f'等待 {seconds} 秒')

# 调用的是最先定义的 wait 函数
wait(3)

# 该函数将覆盖之前定义的 wait
def wait(hours, minutes=5):
    print(f'等待 {hours} 小时 {minutes} 分')

# 调用的是最后定义的 wait 函数
wait(3)

# 在模块中定义变量 message
message = '我是一个模块变量'

# 函数 show 定义了自己的 message
def show():
    # 这并不会修改模块定义的 message
    message = '我是函数中的变量'
    print(message)

# 函数 show_again 使用了模块定义的 message
def show_again():
    print(message)

show()
show_again()

# 一个简单的函数
def simple(a: int = 1) -> None:
    '''一个简单的函数~~~！

    果然，很简单。
    '''

# 计算元组中所有小于等于 10 的数字之和
def add_list(*l):
    # 嵌套函数 check，检查数字，大于 10 则返回 0
    def check(i):
        return 0 if i > 10 else i
    
    # 调用 check，忽略元组中大于 10 的数字
    num = 0
    for i in l:
        num += check(i)

    return num

print(add_list(4, 2, 11, 3))

# 使用 lambda 表达式定义匿名函数
div = lambda a, b: a / b

print(div(9, 3))