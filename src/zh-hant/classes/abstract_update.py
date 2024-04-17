from abc import ABC, abstractmethod, update_abstractmethods

# 定義抽象基底類別 Color 和衍生類別 Black
class Color(ABC):
    pass
class Black(Color):
    pass

# 動態的為抽象基底類別增加一個抽象方法
@abstractmethod
def show(self):
    pass
Color.show = show

print(f'建立第一個 Black 執行個體')
# 建立執行個體沒有問題
Black()

# 更新抽象類別 Color 和 Black
update_abstractmethods(Color)
update_abstractmethods(Black)
print(f'建立第二個 Black 執行個體')
# ERROR 不能建立執行個體，因為 Black 沒有實作抽象方法 show
Black()
