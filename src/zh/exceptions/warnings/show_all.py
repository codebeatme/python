import warnings

# ImportWarning 在默认规则中不会显示
warnings.warn('默认不会显示的警告', ImportWarning)

# 临时让所有警告均被显示
with warnings.catch_warnings(action='always'):
    warnings.warn('现在可以显示 ImportWarning', ImportWarning)

# 查看匹配规则的第一条
print(warnings.filters[0])