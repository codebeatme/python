# 一個表示學生的類別 Student
class Student:
    # 類別變數 count
    count = 0
    # 建構子
    def __init__(self, n, a):
        # 執行個體變數 name，age
        self.name = n
        self.age = a

    # 執行個體方法 info
    def info(self):
        print(f'{self.name} {self.age}')

    # 類別方法 show
    @classmethod
    def show(cls):
        # 通過參數 cls 讀取類別變數 count
        print(f'一共 {cls.count} 個學生')
        
    # 靜態方法 set_count
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

# 取得 Student 類別和之前建立的執行個體 student 的型別資訊
print(student.__class__)
print(Student.__class__)