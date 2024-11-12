# 自訂 with 陳述式內容管理器 CM
class CM:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(exc_type, exc_value, exc_tb)
        # 傳回 True 後，例外狀況將被抑製
        return True

with CM():
    # 例外狀況 ZeroDivisionError 被引發並且沒有得到處理
    num = 1 / 0
