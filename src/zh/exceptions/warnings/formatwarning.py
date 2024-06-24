import warnings

# 用于格式化警告信息的函数 myinfo
def myinfo(message, category, filename, lineno, line=None):
    
    # 处理 line 参数为 None 的情况
    if not line:
        line = open(filename, encoding='utf8').readlines()[lineno - 1]

    return f'简化的信息：{line} {category} {message}'

# 用 myinfo 替换原有的 formatwarning 函数
warnings.formatwarning = myinfo
warnings.warn('一个警告')
