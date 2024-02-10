# 定義一個具有參數 name 的函式 hello
def hello(name):
    '''一個超級簡單的函式'''
    print(f'你好，{name}')

# 呼叫函式 hello
hello('Kitty')

# 定義加法函式
def add(x=1, y=[], /, *, z):
    # 串列 y 新增數值 100
    y.append(100)
    print(y)

    # 計算 x，y，z 含有的數值之和
    num = 0
    for i in y:
        num += i

    return x + num + z

# z 只能作為關鍵字參數使用
print(add(z=1))
# x 作為位置參數被使用
print(add(1, z=3))

# 定了乘法函式
def mlp(*nums, **info):
    # 顯示關鍵字參數
    print(info)

    # 計算 nums 中包含的位置參數
    num = 1
    for i in nums:
        num *= i

    return num

# 傳遞了多個數值進行乘法計算
print(mlp(2, 3, 4, 5, tip='這裏是一個小小的提示'))

# 在模組中定義變數 message
message = '我是一個模組變數'

# 函式 show 定義了自己的 message
def show():
    # 這並不會修改模組定義的 message
    message = '我是函式中的變數'
    print(message)

# 函式 show_again 使用了模組定義的 message
def show_again():
    print(message)

show()
show_again()

# 一個簡單的函式
def simple(a: int = 1) -> None:
    '''一個簡單的函式~~~！

    果然，很簡單。
    '''

# 計算元組中所有小於等於 10 的數值之和
def add_list(*l):
    # 巢狀函式 check，檢查數值，大於 10 則傳回 0
    def check(i):
        return 0 if i > 10 else i
    
    # 呼叫 check，忽略元組中大於 10 的數值
    num = 0
    for i in l:
        num += check(i)

    return num

print(add_list(4, 2, 11, 3))

# 使用 lambda 運算式定義匿名函式
div = lambda a, b: a / b

print(div(9, 3))