  # 一個關於人的類別
class Person:
    title = '該如何稱呼哪？'

    def __init__(self, name, age):
        # 定義類別的執行個體變數 name，age
        self.name = name
        self.age = age

# 表示好人的類別，從 Person 繼承
class GoodMan(Person):
    pass

# 建立 GoodMan 的執行個體
goodman = GoodMan('好心人', 40)

# 判斷執行個體 goodman 的型別是否為 Person 或 int
print(isinstance(goodman, (Person, int)))
# 判斷執行個體 goodman 的型別是否為 int，float，str 中的一個
print(isinstance(goodman, int | float | str))

# 判斷類別 GoodMan 是否為 object 的子類別
print(issubclass(GoodMan, object))
# 判斷類別 GoodMan 是否為 str 或 Person 的子類別
print(issubclass(GoodMan, str | Person))
# 判斷類別 GoodMan 是否為 GoodMan 的子類別
print(issubclass(GoodMan, GoodMan))