'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-and-access-class-static-fields/ 如何定義和存取類別的靜態欄位
'''

###
import random


class Unit:
    # 類別 Unit，表示遊戲中的單位

    # 靜態欄位 count，表示存活單位的個數
    count = 0

    def __init__(self, hp):
        # 設定單位的初始狀態，包括生命值，死亡狀態
        self.hp = hp
        self.dead = False
        # 存活單位的個數加 1
        Unit.count += 1

    ###
    def hurt(self, damage):
        # 讓單位受傷的方法

        # 根據傷害扣除生命值
        self.hp -= damage
        print(f'一個單位受到 {damage} 點傷害')

        # 生命值小於等於 0，則認為單位死亡，存活單位的個數減 1
        if self.hp <= 0:
            self.dead = True
            Unit.count -= 1
            print(f'一個單位死亡，剩余 {Unit.count} 個單位')


### 建立三個遊戲單位，狀態為存活
units = [Unit(10), Unit(15), Unit(20)]
game_over = False

while not game_over:

    # 依次讓所有存活單位受到傷害，直到僅剩一個存活單位時
    for unit in units:
        if not unit.dead:
            # 傷害大小是隨機的
            damage = random.randint(0, 10)
            unit.hurt(damage)

            # 僅剩一個存活單位，則跳出迴圈，遊戲結束
            if Unit.count == 1:
                game_over = True
                break

print('遊戲結束')

# 定義靜態欄位 type_name，表示 Unit 的類別名稱
Unit.type_name = '單位'
print(f'Unit 的類別名稱為：{Unit.type_name}')
