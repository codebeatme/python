# A class on plants
class Plant:
    # Class variable variety
    variety = 'Unknown'

    def __init__(self, name):
        # Instance variable name
        self.name = name

# A class that inherits from the Plant class
class Tree(Plant):

    # Methods of displaying information
    def show(self):
        print(self.name)

tree = Tree('Large tree')
tree.show()
print(f'Tree: What kind? {Tree.variety}')

# age does not exist, and writing it is equivalent to adding an instance variable to the tree
tree.age = 100
print(tree.age)
# ERROR The class variable name does not exist, and reading it will cause an exception
print(Tree.name)
