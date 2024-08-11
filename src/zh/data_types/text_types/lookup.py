# 一个转换表类
class Trans:
    def __getitem__(self, key):
        # 如果是 A，则保持不变
        if key == 65:
            raise LookupError()
        
        # 转换为编码值加 1 的字符
        return key + 1
    
print('ABC'.translate(Trans()))