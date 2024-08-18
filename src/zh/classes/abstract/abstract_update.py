from abc import ABC, abstractmethod, update_abstractmethods

# 定义抽象基类 Color 和派生类 Black
class Color(ABC):
    pass
class Black(Color):
    pass

# 动态的为抽象基类增加一个抽象方法
@abstractmethod
def show(self):
    pass
Color.show = show

print('创建第一个 Black 实例')
# 创建实例没有问题
Black()

# 更新抽象类 Color 和 Black
update_abstractmethods(Color)
update_abstractmethods(Black)
print('创建第二个 Black 实例')
# ERROR 不能创建实例，因为 Black 没有实现抽象方法 show
Black()
