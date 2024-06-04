try:
    import random
    # 有一定的几率引发异常 Exception
    if random.randint(0, 1):
        raise Exception()
except:
    # 至少需要一个 except，才能书写 else
    print('哎呀！一个错误')
else:
    # 仅在没有异常时执行
    print('居然没有错误！')

def run():
    try:
        # 执行 return 将导致 else 语句被忽略
        return
    except:
        pass
    else:
        # 这里的语句不会被执行
        print('太好了，没有错误')

run()