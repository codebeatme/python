'''
本節文章
https://learnscript.net/zh-hant/python/advanced/reading-and-writing-files/ 如何讀取和寫入檔案
'''

###


class Student:
    # 類別 Student，表示一個學生

    def __init__(self, n, a):
        # 定義欄位表示學生的姓名，年齡
        self.name = n
        self.age = a


# 從檔案 D:/student.txt 讀取學生資訊
students = []

file = open('D:/student.txt', 'r')
lines = file.readlines()
file.close()

# 將從檔案讀取的每一行轉換為學生物件
for line in lines:
    # 忽略空行
    if line:
        args = line.split(' ')
        name = args[0]
        age = int(args[1])

        students.append(Student(name, age))

while True:
    # 要求輸入學生的相關資訊
    text = input('請輸入姓名和年齡，使用空格分割：')

    # n 表示結束輸入
    if text == 'n':
        break

    # 使用輸入的學生資訊，建立 Student 類別的執行個體，並儲存到串列
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])

    student = Student(input_name, input_age)

    students.append(student)

# 將學生資訊轉換為字串，並儲存到串列 lines
lines = []

for s in students:
    lines.append(f'{s.name} {s.age}\n')
    print(f'學生{s.name} 年齡 {s.age}')

# 將串列 lines 寫入到檔案 D:/student.txt
file = open('D:/student.txt', 'w')
file.writelines(lines)
file.close()
