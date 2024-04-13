# 一个关于植物的类
class Plant:
    # 类变量 variety
    variety = '未知种类'

    def __init__(self, name):
        # 实例变量 name
        self.name = name

# 继承自 Plant 类的类
class Tree(Plant):

    # 显示信息的方法
    def show(self):
        print(self.name)

tree = Tree('大树')
tree.show()
print(f'Tree 是什么种类？{Tree.variety}')

# age 并不存在，写入操作等于为 tree 增加实例变量
tree.age = 100
print(tree.age)
# ERROR 类变量 name 并不存在，读取操作将导致异常
print(Tree.name)
