def no_exception(r):
    try:
        # 引發例外狀況 AttributeError
        raise AttributeError()
    finally:
        if r:
            print('呼叫了 return 陳述式')
            # 這裏的 return 陳述式將導致未處理的例外狀況不被擲回
            return
        else:
            print('沒有呼叫 return 陳述式')

# 不會顯示錯誤資訊
no_exception(True)
# 會顯示錯誤資訊
no_exception(False)