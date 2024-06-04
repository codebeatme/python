from abc import ABC, abstractmethod, get_cache_token

# 定义抽象基类 Man
class Man(ABC):
    @abstractmethod
    def run(self):
        pass

# 将类 Jerry 和 Tom 注册为虚派生类，并查看令牌的变化
print(f'令牌为 {get_cache_token()}')

@Man.register
class Jerry():
    pass

print(f'令牌为 {get_cache_token()}')

class Tom():
    def run(self):
        # ERROR Man 不在 MRO 中
        super().run()
Man.register(Tom)

print(f'令牌为 {get_cache_token()}')

# Jerry 和 Tom 被认为是派生类
print(issubclass(Jerry, Man))
print(issubclass(Tom, Man))
# 可以正常创建实例
print(isinstance(Jerry(), Man))
print(isinstance(Tom(), Man))

Tom().run()