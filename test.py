# 一个用于构造邮箱正则表达式的字符串
pattern = (
    '\\b[\\w.%-]+' # 邮箱中 @ 前的部分
    '@' # 邮箱中的 @
    '[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}' # 邮箱中 @ 后的部分
)

import re
print(re.search(pattern, "xiao_xiao" '@'    '''live.com'''))

print(type(1+3j).__str__('d11'))
print(repr(1+3j))
bytes
bytearray
import array
a = array.array[int]()
a.append(12)
memoryview
str(array.array())
float