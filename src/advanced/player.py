class Player:

    def __init__(me):
        me.hp = 100

p1 = Player()
p2 = Player()

p1.hp -= 10
p2.hp -= 20

print(f'玩家1剩余生命值{p1.hp}')
print(f'玩家2剩余生命值{p2.hp}')