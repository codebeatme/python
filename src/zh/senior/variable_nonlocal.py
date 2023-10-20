'''
在内部函数中使用nonlocal关键字，可以让内部函数修改上级函数中的变量
* nonlocal后跟随变量名，即可修改对应的上级函数中定义的变量
* nonlocal无法定位模块定义的变量或者类的字段

版本
Python 3.11.1
VSCode 1.76.0

关于本系列教程的使用说明和相关问题解答，请参考文章 https://www.bilibili.com/read/cv23030766
'''

###
defence = 10

###
def hurt(damage):
    global defence
    damage -= defence
    defence -= 1
    
    ###
    def defence_break():
        nonlocal damage

        if damage > 50:
            global defence
            defence = 0
            damage = 1
            print('高伤害已经使防御值降为0，但本次伤害降为1')

    defence_break()
    ###

    if damage <= 0:
        return

    def show(text):
        print(text)

    message = f'考虑防御值后的伤害为{damage}'
    show(message)

###
hurt(100)
hurt(15)
hurt(15)
