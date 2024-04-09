
# 判斷 import.py 是否為程式進入點
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


# 通過模組呼叫所謂的私用特性
t._add_avg_age(1)
print(f'現在的平均年齡是 {t.__avg_age}')

