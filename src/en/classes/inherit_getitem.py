# A class that represents a store
class Store:
    def __getitem__(self, key):
        print(f'Want to get items? {key}')
        return key
    
# A class that represents the app store
class AppStore(Store):
    pass

store = AppStore()
# You can use the [] operator on instances
x = store['x']
# For super, you need to use the . operator
y = super(AppStore, store).__getitem__('y')
# ERROR Using the [] operator for super will result in an exception
z = super(AppStore, store)['z']