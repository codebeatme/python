# 一個關於植物的類別
class Plant:
    # 類別變數 variety
    variety = '未知種類'

    def __init__(self, name):
        # 執行個體變數 name
        self.name = name

# 繼承自 Plant 類別的類別
class Tree(Plant):

    # 顯示資訊的方法
    def show(self):
        print(self.name)

tree = Tree('大樹')
tree.show()
print(f'Tree 是什麽種類？{Tree.variety}')

# age 並不存在，寫入操作等於為 tree 增加執行個體變數
tree.age = 100
print(tree.age)
# ERROR 類別變數 name 並不存在，讀取操作將導致例外狀況
print(Tree.name)
