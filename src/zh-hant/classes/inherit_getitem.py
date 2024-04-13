# 一個表示商店的類別
class Store:
    def __getitem__(self, key):
        print(f'想獲得物品？{key}')
        return key
    
# 一個表示應用商店的類別
class AppStore(Store):
    pass

store = AppStore()
# 可以對執行個體使用 [] 運算子
x = store['x']
# 對 super 需要使用 . 運算子
y = super(AppStore, store).__getitem__('y')
# ERROR 對 super 使用 [] 運算子，將導致例外狀況
z = super(AppStore, store)['z']