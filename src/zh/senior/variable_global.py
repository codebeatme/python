'''
模块中定义的变量，无法在函数或方法中直接修改，需要使用global关键字
* 在函数中书写global后跟随模块变量名，之后便可对模块变量修改

版本
Python 3.11.1
VSCode 1.76.0

关于本系列教程的使用说明和相关问题解答，请参考文章 https://www.bilibili.com/read/cv23030766
'''

###
defence = 10

###
def hurt(damage):
    # defence = 14
    global defence
    damage -= defence
    defence -= 1
    
    if damage <= 0:
        return

    def show(text):
        print(text)

    message = f'考虑防御值后的伤害为{damage}'
    show(message)

    global health_point
    health_point = 100

###
hurt(15)
hurt(15)
print(health_point)