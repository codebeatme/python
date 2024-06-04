from abc import ABC, abstractmethod, get_cache_token

# 定義抽象基底類別 Man
class Man(ABC):
    @abstractmethod
    def run(self):
        pass

# 將類別 Jerry 和 Tom 註冊為虛擬衍生類別，並檢視權杖的變化
print(f'權杖為 {get_cache_token()}')

@Man.register
class Jerry():
    pass

print(f'權杖為 {get_cache_token()}')

class Tom():
    def run(self):
        # ERROR Man 不在 MRO 中
        super().run()
Man.register(Tom)

print(f'權杖為 {get_cache_token()}')

# Jerry 和 Tom 被認為是衍生類別
print(issubclass(Jerry, Man))
print(issubclass(Tom, Man))
# 可以正常建立執行個體
print(isinstance(Jerry(), Man))
print(isinstance(Tom(), Man))

Tom().run()