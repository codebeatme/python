player_life = 10
enemy_life = 10

player_ap = 1
enemy_ap = 3

while True:
    enemy_life -= player_ap
    print(f'敌人受到玩家{player_ap}点伤害，剩余{enemy_life}点生命')

    if enemy_life <= 0:
        print('敌人死亡，获得胜利')
        break

    player_life -= enemy_ap
    print(f'玩家受到敌人{enemy_ap}点伤害，剩余{player_life}点生命')

    if player_life <= 0:
        print('玩家死亡，任务失败')
        break