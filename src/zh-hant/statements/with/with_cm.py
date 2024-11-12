# 模組變數 students
students = ['小紅', '小黑']

# 自訂 with 陳述式內容管理器 CM
class CM:
    def __enter__(self):
        # 將模組變數 students 中的串列儲存到 CM 中
        global students
        self.students = students

        # 將新的串列指派給模組變數 students
        students = ['小蘭', '小白']
        return students
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        # 恢復模組變數 students 中原有的串列
        global students
        students = self.students

# CM 會臨時改變模組變數 students
with CM() as s:
    print(s, students)

print(students)