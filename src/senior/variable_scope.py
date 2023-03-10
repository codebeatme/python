# 视频内容：「Python」高级教程 什么是变量的作用域？变量的作用范围和检索顺序
# 视频地址：https://www.bilibili.com/video/BV1JN411c7ML/

###
defence = 10

###
def hurt(damage):
    # defence = 14
    damage -= defence
    
    if damage <= 0:
        return

    def show(text):
        print(text)

    message = f'考虑防御值后的伤害为{damage}'
    show(message)

###
hurt(15)