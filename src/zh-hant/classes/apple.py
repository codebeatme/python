# 一個簡單的類別 Apple
class Apple:
    # 變數 variety
    variety = '普通蘋果'
    # 靜態方法 show
    @staticmethod
    def show():
        print(Apple.variety)

    # 建構子
    def __init__(self, w):
        # 通過表示執行個體的 self 定義了執行個體變數 weight
        self.weight = w

# 為特性 variety 指派
Apple.variety = '石頭蘋果'
# 呼叫 show 方法
Apple.show()

# 為 Apple 類別新增一個類別變數，然後顯示 Apple 類別的所有特性
Apple.price = 10
print(Apple.__dict__)
# 為執行個體新增一個執行個體變數，然後顯示執行個體的所有特性
apple = Apple(100)
apple.price = 30
print(apple.__dict__)

# 建立 Apple 類別的執行個體
apple = Apple(30)
# 通過執行個體存取類別變數 variety
print(apple.variety)

# 下面的指派陳述式將為執行個體定義新的執行個體變數 variety
apple.variety = '超大蘋果'
# 因此，類別變數 variety 並沒有變化
print(Apple.variety)