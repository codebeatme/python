# 一个用于生成邮箱正则表达式的字符串
pattern = (
	'\\b[\\w.%-]+' # 邮箱中 @ 前面的部分
	'@' # 邮箱中的 @
	'[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}' # 邮箱中 @ 后面的部分
)

import re
print(re.search(pattern, "xiao_xiao" '@'	'''live.com'''))
