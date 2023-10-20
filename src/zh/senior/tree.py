'''
本节文章
https://learnscript.net/zh/python/senior/judge-application-entry-point/ 如何判断程序入口点
'''

print('这里是关于树的模块！')

class Tree:
    # 类 Tree，表示一棵树

    def __init__(self, name, height):
        # 大树的名字，高度
        self.name = name
        self.height = height

    def show_info(self):
        # 显示大树的相关信息
        print(f'大树 {self.name} 高 {self.height} 米')

# 判断是否是程序入口点
if __name__ == '__main__':
    print('让我们创建一些树！')
    # 创建一个树的元组
    trees = (
        Tree('大个子', 5.8),
        Tree('小个子', 2.1)
    )

    # 显示所有树的信息
    for tree in trees:
        tree.show_info()