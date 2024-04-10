# 一个简单的类 Apple
class Apple:
    # 变量
    variety = '普通苹果'
    # 静态方法
    @staticmethod
    def show():
        print(Apple.variety)

    # 构造器
    def __init__(self, w):
        # 通过表示实例的 self 定义了实例变量 weight
        self.weight = w

# 为特性 variety 赋值
Apple.variety = '石头苹果'
# 调用 show 方法
Apple.show()

# 为 Apple 类添加一个类变量，然后显示 Apple 类的所有特性
Apple.price = 10
print(Apple.__dict__)
# 为实例添加一个实例变量，然后显示实例的所有特性
apple = Apple(100)
apple.price = 30
print(apple.__dict__)

# 创建 Apple 类的实例
apple = Apple(30)
# 通过实例访问类变量 variety
print(apple.variety)

# 下面的赋值语句将为实例定义新的实例变量 variety
apple.variety = '超大苹果'
# 因此，类变量 variety 并没有变化
print(Apple.variety)