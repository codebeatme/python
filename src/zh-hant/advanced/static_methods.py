'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-and-call-class-static-methods/ 如何定義和呼叫類別的靜態方法
'''

###


class Unit:
    # 類別 Unit，表示遊戲單位

    # 靜態欄位，表示單位數量
    count = 0

    ###
    @staticmethod
    def random_id():
        # 靜態方法 random_id，用於產生一個隨機 id
        import random
        num = random.randint(1, 10000000)
        return f'id_{num}'

    ###
    @classmethod
    def show_info(cls):
        # 靜態方法 show_info，用來顯示一些資訊
        print(f'總計 {cls.count} 個單位')

    ###
    def __init__(self, hp):
        # 產生一個隨機 id，並儲存在 id 欄位中
        self.id = self.random_id()
        self.hp = hp
        Unit.count += 1


###
# 建立 Unit 類別的執行個體
unit = Unit(100)
print(f'unit.id={unit.id}')
# 通過類別呼叫靜態方法
Unit.show_info()
