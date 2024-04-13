# 一个表示商店的类
class Store:
    def __getitem__(self, key):
        print(f'想获得物品？{key}')
        return key
    
# 一个表示应用商店的类
class AppStore(Store):
    pass

store = AppStore()
# 可以对实例使用 [] 运算符
x = store['x']
# 对 super 需要使用 . 运算符
y = super(AppStore, store).__getitem__('y')
# ERROR 对 super 使用 [] 运算符，将导致异常
z = super(AppStore, store)['z']