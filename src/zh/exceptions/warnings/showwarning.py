import warnings

# 第 4 行代码将作为警告信息的一部分
message = '直接调用 showwarning'
warnings.showwarning(
    message, UserWarning,
    filename=__file__, lineno=4
)

# 用于显示警告的函数 mywarning
def mywarning(message, category, filename, lineno, file=None, line=None):
    
    # 处理 file，line 参数为 None 的情况
    if not file:
        import sys
        file = sys.stderr

    if not line:
        line = open(filename, encoding='utf8').readlines()[lineno - 1]

    file.writelines(f'自定义警告：{message} {category} {line}')

# 用 mywarning 替换原有的 showwarning 函数
warnings.showwarning = mywarning
warnings.warn('再次警告')
