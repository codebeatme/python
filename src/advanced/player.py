# 视频内容：「Python」进阶教程 类有什么作用？如何定义和使用类
# 视频地址：https://www.bilibili.com/video/BV13b411X7Za/

class Player:

    def __init__(me):
        me.hp = 100

p1 = Player()
p2 = Player()

p1.hp -= 10
p2.hp -= 20

print(f'玩家1剩余生命值{p1.hp}')
print(f'玩家2剩余生命值{p2.hp}')
