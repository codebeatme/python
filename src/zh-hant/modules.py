
# 判斷 modules.py 是否為程式進入點
if __name__ == '__main__':
	# 顯示模組的檔案路徑
	print(__file__)

# 匯入模組 teacher
import school.teacher
# 通過 __dict__ 讀取 teacher 的 count 特性
print(school.teacher.__dict__['count'])

# 使用 as 關鍵字指定識別碼
import school.teacher as t

# 可以通過 t 來使用 teacher 模組
t.count = 100
t.show()

# teacher 模組的特性 count，level，show 將被繫結至當前命名空間
from school.teacher import *

# 由於之前使用 t.count = 100 修改了特性，這裏將顯示為 100
print(f'我在模組 modules 中讀取的教師數量為 {count}')
show()

# 這裏會定義新的變數 level，而不是對 teacher 中的 level 指派
level = 100
# 之前 t 已經繫結至模組 teacher
print(f'教師的層級為 {t.level}')

# 由於 teacher 模組已經被匯入，因此他是套件 school 的特性
from school import *

# 這裏可以使用 teacher
print(teacher)
# ERROR 存取模組 student 會導致例外狀況
print(student)