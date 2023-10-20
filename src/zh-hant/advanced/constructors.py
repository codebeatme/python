'''
本節文章
https://learnscript.net/zh-hant/python/advanced/define-class-constructors/ 如何定義類別的建構方法
'''


class Teacher:
    # 類別 Teacher，表示了教師

    def __init__(self, n, a):
        # 建構方法，使用參數 n，a，初始化欄位 name，age
        self.name = n
        self.age = a


# 建立 Teacher 類別的執行個體，並設定姓名和年齡
teachers = (
    Teacher('鋼鐵俠', 40),
    Teacher('超人', 30),
    Teacher('普通人', 20),
    Teacher('一個嬰兒', 1),
)

for t in teachers:
    print(f'教師：{t.name} 年齡：{t.age}')
