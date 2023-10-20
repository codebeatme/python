'''
本节文章
https://learnscript.net/zh/python/advanced/define-class-constructors/ 如何定义类的构造方法
'''


class Teacher:
    # 类 Teacher，表示了教师

    def __init__(self, n, a):
        # 构造方法，使用参数 n，a，初始化字段 name，age
        self.name = n
        self.age = a


# 创建 Teacher 类的实例，并设置姓名和年龄
teachers = (
    Teacher('钢铁侠', 40),
    Teacher('超人', 30),
    Teacher('普通人', 20),
    Teacher('一个婴儿', 1),
)

for t in teachers:
    print(f'教师：{t.name} 年龄：{t.age}')
