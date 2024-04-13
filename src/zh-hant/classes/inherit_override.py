# 一個遊戲單位
class Unit:
    # 用於發起攻擊的方法
    def attack(self):
        print('Unit 發起攻擊')

class Hero(Unit):
    # 該方法將被之後定義的 attack 覆蓋
    def attack(self, times):
        while times > 0:
            print('Hero 發起攻擊')
            times -= 1

    # 將覆寫 Unit 的 attack 方法，並覆蓋之前定義的 attack
    def attack(self, times):
        print(f'Hero 將發起 {times} 次攻擊')

Unit().attack()
Hero().attack(5)
# ERROR 無法呼叫 Unit 類別定義的 attack 方法
Hero().attack()