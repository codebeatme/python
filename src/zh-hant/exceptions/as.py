import sys
# 該變數稍後會被刪除
err = 'error'

try:
    # 除數為 0 將引發例外狀況 ZeroDivisionError
    1 / 0
except ZeroDivisionError as err:
    # 通過識別碼 err 和 exception 函式取得的例外狀況物件相同
    print(sys.exception() == err)

print(sys.exception())
print(err)
