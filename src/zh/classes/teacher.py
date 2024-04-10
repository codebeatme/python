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