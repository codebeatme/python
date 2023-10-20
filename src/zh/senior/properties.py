'''
本节文章
https://learnscript.net/zh/python/senior/define-class-properties/ 如何定义类的属性
'''

class Worker:
    # 类 Worker，表示一位员工

    def __init__(self, name, title):
        # 员工的姓名和头衔
        self.name = name
        self.title = title

    @property
    def full_title(self):
        # 属性 full_title，表示员工的全称，由头衔和姓名组成
        return f'{self.title} {self.name}'

    @full_title.setter
    def full_title(self, value):
        # 写入属性，value 是一个包含头衔和姓名的字符串

        # 头衔和姓名之间使用了空格，可以作为分割的依据
        args = value.split(' ')
        # 将新值中包含的头衔和姓名，分别赋值给 title，name 字段
        self.title = args[0]
        self.name = args[1]


# 创建 Worker 类的实例 worker
worker = Worker('汤姆', '捕鼠大师')

# 读取属性 full_title，并显示
print(f'来了一位新的员工：{worker.full_title}')

# 写入属性 full_title，然后再次显示
worker.full_title = '耍猫大师 杰瑞'
print(f'哦！搞错了，抱歉，新员工是：{worker.full_title}')
