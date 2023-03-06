# 视频内容：「Python」高级教程 nonlocal有什么用？内部函数如何修改上级函数的变量
# 视频地址：https://www.bilibili.com/video/BV1Bo4y1z7uD/

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
