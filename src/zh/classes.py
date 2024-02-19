# 一个简单的类 Apple
class Apple:
    # 变量
    name = '苹果'
    # 静态方法
    @staticmethod
    def show():
        print(Apple.name)

    # 构造器
    def __init__(self, w):
        # 通过表示实例的 self 定义了实例变量 weight
        self.weight = w
        

# 为特性 name 赋值
Apple.name = '一个苹果'
# 调用 show 方法
Apple.show()

# 为 Apple 类添加一个类变量
Apple.price = 10
# 分别显示 Apple 类和 Apple 实例的特性
print(Apple.__dict__)
print(Apple(100).__dict__)

# 创建 Apple 类的实例
apple = Apple(30)
# 通过实例访问类变量 name
print(apple.name)

# 下面的赋值语句将为实例定义新的实例变量 price
apple.price = 100
# 因此，类变量 price 并没有变化
print(Apple.price)

# 一个表示学生的类 Student
class Student:
    # 类变量
    count = 0
    # 构造器
    def __init__(self, n, a):
        # 实例变量 name，age
        self.name = n
        self.age = a

    # 实例方法
    def info(self):
        print(f'{self.name} {self.age}')

    # 类方法
    @classmethod
    def show(cls):
        # 通过参数 cls 读取类变量
        print(f'一共 {cls.count} 个学生')
        
    # 静态方法
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

# 一个表示教师的类 Teacher
class Teacher:
	# 构造器
	def __init__(self, n, a):
		# 私有实例变量 __name，__age
		self.__name = n
		self.__age = a

teacher = Teacher('隐者', 30)
# 显示 Teacher 实例的所有特性
print(teacher.__dict__)
# 使用特殊方式访问私有变量 __name
print(teacher._Teacher__name)

# 一个奇怪的类
class Hello:
    """你好啊，"""'Python！'

    # 一个奇怪的嵌套类
    class World:
        pass