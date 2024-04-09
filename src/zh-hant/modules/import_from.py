# teacher 模組的特性 count，level，show 將被繫結至當前命名空間
from school.teacher import *

# 此處的 count 指向 teacher 模組的 count 特性
print(f'我在模組 modules 中讀取的教師數量為 {count}')
show()

# 這裏會定義新的變數 count，而不是對 teacher 中的 count 進行指派
count = 100
# 呼叫 show 後，並不會顯示 100
show()

# ERROR * 並不會匯入私用特性
# print(__avg_age)


# 由於 teacher 模組之前已經被匯入，因此他是套件 school 的特性
from school import *

# 這裏可以使用 teacher
print(teacher)
# ERROR 存取 school 的子模組 student 會導致例外狀況
print(student)