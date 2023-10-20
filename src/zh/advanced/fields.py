'''
本节文章
https://learnscript.net/zh/python/advanced/define-and-access-class-fields/ 如何定义和访问类的字段
'''


class Tree:
    # 类 Tree，表示一棵树

    def __init__(self):
        # 为字段 age 赋值 0，也就等同于定义了字段 age
        self.age = 0


# 创建 Tree 类的实例
tree = Tree()

# 让用户输入大树的年龄，并将其转换为整型
input_age = int(input('请输入大树的年龄：'))

# 如果输入的年龄合理，则设置
if input_age > 0:
    tree.age = input_age

# 显示大树的年龄
print(f'大树 {tree.age} 岁了！')
