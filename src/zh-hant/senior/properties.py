'''
本節文章
https://learnscript.net/zh-hant/python/senior/define-class-properties/ 如何定義類別的屬性
'''

class Worker:
    # 類別 Worker，表示一位員工

    def __init__(self, name, title):
        # 員工的姓名和頭銜
        self.name = name
        self.title = title

    @property
    def full_title(self):
        # 屬性 full_title，表示員工的全稱，由頭銜和姓名組成
        return f'{self.title} {self.name}'

    @full_title.setter
    def full_title(self, value):
        # 寫入屬性，value 是一個包含頭銜和姓名的字串

        # 頭銜和姓名之間使用了空格，可以作為分割的依據
        args = value.split(' ')
        # 將新值中包含的頭銜和姓名，分別指派給 title，name 欄位
        self.title = args[0]
        self.name = args[1]


# 建立 Worker 類別的執行個體 worker
worker = Worker('湯姆', '捕鼠大師')

# 讀取屬性 full_title，並顯示
print(f'來了一位新的員工：{worker.full_title}')

# 寫入屬性 full_title，然後再次顯示
worker.full_title = '耍貓大師 傑瑞'
print(f'哦！搞錯了，抱歉，新員工是：{worker.full_title}')
