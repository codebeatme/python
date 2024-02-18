
# 判断 modules.py 是否为程序入口点
if __name__ == '__main__':
	# 显示模块的文件路径
	print(__file__)

# 导入模块 teacher
import school.teacher
# 通过 __dict__ 读取 teacher 的 count 特性
print(school.teacher.__dict__['count'])

# 使用 as 关键字指定标识符
import school.teacher as t

# 可以通过 t 来使用 teacher 模块
t.count = 100
t.show()

# teacher 模块的特性 count，level，show 将被绑定至当前命名空间
from school.teacher import *

# 由于之前使用 t.count = 100 修改了特性，这里将显示为 100
print(f'我在模块 modules 中读取的教师数量为 {count}')
show()

# 这里会定义新的变量 level，而不是对 teacher 中的 level 赋值
level = 100
# 之前 t 已经绑定至模块 teacher
print(f'教师的级别为 {t.level}')

# 由于 teacher 模块已经被导入，因此他是包 school 的特性
from school import *

# 这里可以使用 teacher
print(teacher)
# ERROR 访问模块 student 会导致异常
print(student)