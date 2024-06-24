import warnings

# 用於格式化警告資訊的函式 myinfo
def myinfo(message, category, filename, lineno, line=None):
    
    # 處理 line 參數為 None 的情況
    if not line:
        line = open(filename, encoding='utf8').readlines()[lineno - 1]

    return f'簡化的資訊：{line} {category} {message}'

# 用 myinfo 取代原有的 formatwarning 函式
warnings.formatwarning = myinfo
warnings.warn('一個警告')
