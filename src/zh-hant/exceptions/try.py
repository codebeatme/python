
try:
    # 除數為 0 將引發例外狀況 ZeroDivisionError
    num = 1 / 0
except Exception:
    # Exception 是 ZeroDivisionError 的基底類別，這裏的程式碼會被執行
    print('比對到了例外狀況 ZeroDivisionError')
except ZeroDivisionError:
    print('無人問津！')

try:
    # 存取未定義的 undefined，將引發例外狀況 NameError
    print(undefined)
except IOError:
    # IOError 不是 NameError 的基底類別，這裏的程式碼不會執行
    print('出現了 IO 錯誤？不可能')