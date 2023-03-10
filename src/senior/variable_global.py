# 视频内容：「Python」高级教程 函数和方法如何修改模块变量？关键字global的作用以及书写格式
# 视频地址：https://www.bilibili.com/video/BV1bT411e7oa/

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