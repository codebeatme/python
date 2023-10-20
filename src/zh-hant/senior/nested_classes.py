'''
本節文章
https://learnscript.net/zh-hant/python/senior/define-nested-classes/ 如何定義和使用巢狀類別
'''

###


class Student:
    # 類別 Student，表示一個學生

    ###
    class Scores:
        # 巢狀類別 Scores，表示學生的成績

        def __init__(self, scores):
            # 定義欄位表示英語和數學成績
            self.english = int(scores[0])
            self.math = int(scores[1])

        def sum(self):
            # 計算總成績
            return self.english + self.math

    ###
    def __init__(self, name, age, scores):
        # 定義欄位表示學生的姓名，年齡和成績
        self.name = name
        self.age = age
        self.scores = self.Scores(scores)

    def show_info(self):
        # 顯示學生的資訊，包括姓名，年齡和總分數
        print(f'姓名：{self.name} 年齡：{self.age} 總分：{self.scores.sum()}')


### 要求輸入學生的相關資訊
text = input('請輸入姓名和年齡以及成績，使用空格分割：')

# 使用輸入的學生資訊，建立 Student 類別的執行個體
args = text.split(' ')
input_name = args[0]
input_age = int(args[1])
input_scores = args[2:]

student = Student(input_name, input_age, input_scores)

### 顯示學生的資訊
student.show_info()
