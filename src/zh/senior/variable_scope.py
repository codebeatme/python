'''
本节文章
https://learnscript.net/zh/python/senior/variable-scope/ 变量的作用域
'''

# 在模块中定义表示防御值的变量 defence
defence = 10

###


def hurt(damage):
    # 函数 hurt，用来造成伤害

    # 这是 hurt 函数定义的 defence
    # defence = 14
    # 根据防御值来降低伤害值
    damage -= defence

    if damage <= 0:
        return

    def show(text):
        # 嵌套函数 show，用来显示信息
        print(text)

    message = f'考虑防御值后的伤害值为 {damage}'
    show(message)


# 造成 15 点伤害
hurt(15)

# ERROR message 没有定义
# print(message)
