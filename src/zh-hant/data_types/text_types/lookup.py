# 一個轉換表類別
class Trans:
    def __getitem__(self, key):
        # 如果是 A，則保持不變
        if key == 65:
            raise LookupError()
        
        # 轉換為編碼值加 1 的字元
        return key + 1
    
print('ABC'.translate(Trans()))