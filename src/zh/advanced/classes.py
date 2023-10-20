'''
本节文章
https://learnscript.net/zh/python/advanced/define-classes/ 如何定义和使用类
'''


class Player:
    # 类 Player，表示游戏中的玩家

    def __init__(self):
        # 在构造方法中，定义了字段 hp，用来表示玩家的生命值
        self.hp = 100


# 创建 Player 类的实例
player1 = Player()
player2 = Player()

# 扣除生命值
player1.hp -= 10
player2.hp -= 20

# 显示生命值
print(f'玩家 1 剩余生命值 {player1.hp}')
print(f'玩家 2 剩余生命值 {player2.hp}')
