def show():
    try:
        # 傳回之前會執行 finally 中的程式碼
        return '一條訊息'
    finally:
        # 在真正傳回之前，這裏的程式碼將被執行
        print(f'在傳回之前執行！')


print(show())


def div(a, b):
    try:
        # 如果除數為 0，則引發例外狀況 ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        # 這裏的傳回值將被忽略
        return 0
    finally:
        # 這裏是最終的傳回值
        return a / (b + 1)

print(div(2, 0))
