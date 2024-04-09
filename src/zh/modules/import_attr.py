import school

def show_teacher():
    # 标识符 school 绑定在函数的命名空间中
    import school.teacher
    # 通过标识符 school 访问模块 teacher 的 show 函数
    school.teacher.show()

# 调用函数后，teacher 模块将成为 school 的一个特性
show_teacher()
# 通过 school 的特性访问模块 teacher
print(f'Teacher 模块？{school.teacher}')