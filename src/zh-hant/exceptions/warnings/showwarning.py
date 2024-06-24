import warnings

# 第 4 行程式碼將作為警告資訊的一部分
message = '直接呼叫 showwarning'
warnings.showwarning(
    message, UserWarning,
    filename=__file__, lineno=4
)

# 用於顯示警告的函式 mywarning
def mywarning(message, category, filename, lineno, file=None, line=None):
    
    # 處理 file，line 參數為 None 的情況
    if not file:
        import sys
        file = sys.stderr

    if not line:
        line = open(filename, encoding='utf8').readlines()[lineno - 1]

    file.writelines(f'自訂警告：{message} {category} {line}')

# 用 mywarning 取代原有的 showwarning 函式
warnings.showwarning = mywarning
warnings.warn('再次警告')
