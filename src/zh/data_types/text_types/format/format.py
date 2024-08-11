# 一个用于格式化的类
class Data:
    def __getitem__(self, key):
        # 提供姓名和年龄信息
        if key == 'name':
            return 'Jack'
        elif key == 'age':
            return 12

# 使用 {name} 和 {age} 进行引用
print('{name} 的年龄是 {age}'.format_map(Data()))