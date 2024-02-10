'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-and-access-class-fields/ 如何定義和存取類別的欄位
'''


class Tree:
    # 類別 Tree，表示一棵樹

    def __init__(self):
        # 為欄位 age 指派 0，也就等同於定義了欄位 age
        self.age = 0


# 建立 Tree 類別的執行個體
tree = Tree()

# 讓使用者輸入大樹的年齡，並將其轉換為整數型別
input_age = int(input('請輸入大樹的年齡：'))

# 如果輸入的年齡合理，則設定
if input_age > 0:
    tree.age = input_age

# 顯示大樹的年齡
print(f'大樹 {tree.age} 歲了！')
