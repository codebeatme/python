# 一個表示教師的類別 Teacher
class Teacher:
    # 建構子
    def __init__(self, n, a):
        # 私用執行個體變數 __name，__age
        self.__name = n
        self.__age = a

teacher = Teacher('隱者', 30)
# 顯示 Teacher 執行個體的所有特性
print(teacher.__dict__)
# 使用特殊方式存取私用變數 __name
print(teacher._Teacher__name)