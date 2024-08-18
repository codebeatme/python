import string
f = string.Formatter()
print(f.format('{name} {0}', 12, name='Jack'))
print(f.vformat(''))