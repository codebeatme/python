'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-and-call-class-methods/ 如何定義和呼叫類別的方法
'''

###


class Student:
    # 類別 Student，表示一個學生

    def __init__(self):
        # 定義欄位表示學生的姓名，年齡，分數，並設定預設值
        self.name = '無名氏'
        self.age = 0
        self.scores = []

    def sum_score(self):
        # 方法 sum_score，用來計算總分數
        total = 0

        # 將欄位 scores 包含的所有分數相加
        for score in self.scores:
            total += int(score)

        return total


###
students = []

while True:
    # 要求輸入學生的相關資訊
    text = input('請輸入姓名和年齡以及分數，使用空格分割：')

    # n 表示結束輸入
    if text == 'n':
        break

    ### 使用輸入的學生資訊，建立 Student 類別的執行個體，並儲存到串列
    args = text.split(' ')

    input_name = args[0]
    input_age = int(args[1])
    input_scores = args[2:]

    student = Student()
    # 依次設定欄位
    student.name = input_name
    student.age = input_age
    student.scores = input_scores

    students.append(student)

###
for s in students:
    # 呼叫方法 sum_score，取得該學生的總分數
    total_score = s.sum_score()
    print(f'學生：{s.name} 年齡：{s.age} 總分數：{total_score}')
