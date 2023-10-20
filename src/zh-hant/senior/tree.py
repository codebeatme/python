'''
本節文章
https://learnscript.net/zh-hant/python/senior/judge-application-entry-point/ 如何判斷程式進入點
'''

print('這裏是關於樹的模組！')

class Tree:
    # 類別 Tree，表示一棵樹

    def __init__(self, name, height):
        # 大樹的名字，高度
        self.name = name
        self.height = height

    def show_info(self):
        # 顯示大樹的相關資訊
        print(f'大樹 {self.name} 高 {self.height} 米')

# 判斷是否是程式進入點
if __name__ == '__main__':
    print('讓我們建立一些樹！')
    # 建立一個樹的元組
    trees = (
        Tree('大個子', 5.8),
        Tree('小個子', 2.1)
    )

    # 顯示所有樹的資訊
    for tree in trees:
        tree.show_info()