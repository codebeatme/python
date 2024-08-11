# 一個用於格式化的類別
class Data:
    def __getitem__(self, key):
        # 提供姓名和年齡資訊
        if key == 'name':
            return 'Jack'
        elif key == 'age':
            return 12

# 使用 {name} 和 {age} 進行參考
print('{name} 的年齡是 {age}'.format_map(Data()))