'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-classes/ 如何定義和使用類別
'''


class Player:
    # 類別 Player，表示遊戲中的玩家

    def __init__(self):
        # 在建構方法中，定義了欄位 hp，用來表示玩家的生命值
        self.hp = 100


# 建立 Player 類別的執行個體
player1 = Player()
player2 = Player()

# 扣除生命值
player1.hp -= 10
player2.hp -= 20

# 顯示生命值
print(f'玩家 1 剩余生命值 {player1.hp}')
print(f'玩家 2 剩余生命值 {player2.hp}')
