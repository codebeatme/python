# 一個簡單的類別 Apple
class Apple:
    # 變數
    name = '蘋果'
    # 靜態方法
    @staticmethod
    def show():
        print(Apple.name)

    # 建構子
    def __init__(self, w):
        # 通過表示執行個體的 self 定義了執行個體變數 weight
        self.weight = w
        

# 為特性 name 指派
Apple.name = '一個蘋果'
# 呼叫 show 方法
Apple.show()

# 為 Apple 類別新增一個類別變數
Apple.price = 10
# 分別顯示 Apple 類別和 Apple 執行個體的特性
print(Apple.__dict__)
print(Apple(100).__dict__)

# 建立 Apple 類別的執行個體
apple = Apple(30)
# 通過執行個體存取類別變數 name
print(apple.name)

# 下面的指派陳述式將為執行個體定義新的執行個體變數 price
apple.price = 100
# 因此，類別變數 price 並沒有變化
print(Apple.price)

# 一個表示學生的類別 Student
class Student:
    # 類別變數
    count = 0
    # 建構子
    def __init__(self, n, a):
        # 執行個體變數 name，age
        self.name = n
        self.age = a

    # 執行個體方法
    def info(self):
        print(f'{self.name} {self.age}')

    # 類別方法
    @classmethod
    def show(cls):
        # 通過參數 cls 讀取類別變數
        print(f'一共 {cls.count} 個學生')
        
    # 靜態方法
    @staticmethod
    def set_count(c):
        # 只能通過類別存取類別變數
        Student.count = c
        print(f'學生數量被設定為 {Student.count}')

student = Student('小小', 13)
# 呼叫執行個體方法 info
student.info()
Student.info(student)
# 呼叫靜態方法 set_count
student.set_count(-100)
Student.set_count(100)
# 呼叫類別方法 show
student.show()
Student.show()

Student()

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

# 一個奇怪的類別
class Hello:
    """你好啊，"""'Python！'

    # 一個奇怪的巢狀類別
    class World:
        pass