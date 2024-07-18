# 一个表示学生的类 Student
class Student:
    # 类变量 count
    count = 0
    # 构造器
    def __init__(self, n, a):
        # 实例变量 name，age
        self.name = n
        self.age = a

    # 实例方法 info
    def info(self):
        print(f'{self.name} {self.age}')

    # 类方法 show
    @classmethod
    def show(cls):
        # 通过参数 cls 读取类变量 count
        print(f'一共 {cls.count} 个学生')
        
    # 静态方法 set_count
    @staticmethod
    def set_count(c):
        # 只能通过类访问类变量
        Student.count = c
        print(f'学生数量被设置为 {Student.count}')

student = Student('小小', 13)
# 调用实例方法 info
student.info()
Student.info(student)
# 调用静态方法 set_count
student.set_count(-100)
Student.set_count(100)
# 调用类方法 show
student.show()
Student.show()

# 获取 Student 类和之前创建的实例 student 的类型信息
print(student.__class__)
print(Student.__class__)