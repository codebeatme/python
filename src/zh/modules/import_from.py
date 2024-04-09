# teacher 模块的特性 count，level，show 将被绑定至当前命名空间
from school.teacher import *

# 此处的 count 指向 teacher 模块的 count 特性
print(f'我在模块 modules 中读取的教师数量为 {count}')
show()

# 这里会定义新的变量 count，而不是对 teacher 中的 count 进行赋值
count = 100
# 调用 show 后，并不会显示 100
show()

# ERROR * 并不会导入私有特性
# print(__avg_age)


# 由于 teacher 模块之前已经被导入，因此他是包 school 的特性
from school import *

# 这里可以使用 teacher
print(teacher)
# ERROR 访问 school 的子模块 student 会导致异常
print(student)