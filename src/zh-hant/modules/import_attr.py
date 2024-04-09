import school

def show_teacher():
    # 識別碼 school 繫結在函式的命名空間中
    import school.teacher
    # 通過識別碼 school 存取模組 teacher 的 show 函式
    school.teacher.show()

# 呼叫函式後，teacher 模組將成為 school 的一個特性
show_teacher()
# 通過 school 的特性存取模組 teacher
print(f'Teacher 模組？{school.teacher}')