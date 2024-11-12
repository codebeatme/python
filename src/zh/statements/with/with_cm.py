# 模块变量 students
students = ['小红', '小黑']

# 自定义 with 语句上下文管理器 CM
class CM:
    def __enter__(self):
        # 将模块变量 students 中的列表保存到 CM 中
        global students
        self.students = students

        # 将新的列表赋值给模块变量 students
        students = ['小兰', '小白']
        return students
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        # 恢复模块变量 students 中原有的列表
        global students
        students = self.students

# CM 会临时改变模块变量 students
with CM() as s:
    print(s, students)

print(students)