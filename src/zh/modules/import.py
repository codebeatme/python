
# 判断 import.py 是否为程序入口点
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


# 通过模块调用所谓的私有特性
t._add_avg_age(1)
print(f'现在的平均年龄是 {t.__avg_age}')

