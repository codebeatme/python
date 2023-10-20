# 用 None 來表示 age 中還沒有真正的年齡
age = None

def is_none(target):
    # 分別使用 == 和 is 判斷目標是否為 None

    if target is None:
        print(f'{target} is None')
    else:
        print(f'{target} is not None')

    if target == None:
        print(f'{target}==None')
    else:
        print(f'{target}!=None')

# 判斷 None，0，'' 是否等於 None
is_none(None)
is_none(0)
is_none('')