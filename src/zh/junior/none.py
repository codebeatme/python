'''
本节文章
https://learnscript.net/zh/python/junior/represent-and-judge-null/ 如何表示和判断空值
'''

# 用 None 来表示 age 中还没有真正的年龄
age = None

def is_none(target):
    # 分别使用 == 和 is 判断目标是否为 None

    if target is None:
        print(f'{target} is None')
    else:
        print(f'{target} is not None')

    if target == None:
        print(f'{target}==None')
    else:
        print(f'{target}!=None')

# 判断 None，0，'' 是否等于 None
is_none(None)
is_none(0)
is_none('')