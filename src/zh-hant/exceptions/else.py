try:
    import random
    # 有一定的幾率引發例外狀況 Exception
    if random.randint(0, 1):
        raise Exception()
except:
    # 至少需要一個 except，才能書寫 else
    print('哎呀！一個錯誤')
else:
    # 僅在沒有例外狀況時執行
    print('居然沒有錯誤！')

def run():
    try:
        # 執行 return 將導致 else 陳述式被忽略
        return
    except:
        pass
    else:
        # 這裏的陳述式不會被執行
        print('太好了，沒有錯誤')

run()