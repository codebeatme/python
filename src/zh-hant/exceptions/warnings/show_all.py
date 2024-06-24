import warnings

# ImportWarning 在預設規則中不會顯示
warnings.warn('預設不會顯示的警告', ImportWarning)

# 臨時讓所有警告均被顯示
with warnings.catch_warnings(action='always'):
    warnings.warn('現在可以顯示 ImportWarning', ImportWarning)

# 檢視比對規則的第一條
print(warnings.filters[0])