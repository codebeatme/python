# 一個用於建置電子郵件規則運算式的字串
pattern = (
	'\\b[\\w.%-]+' # 電子郵件中 @ 前面的部分
	'@' # 電子郵件中的 @
	'[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}' # 電子郵件中 @ 後面的部分
)

import re
print(re.search(pattern, "xiao_xiao" '@'	'''live.com'''))

import string
string.capwords()

''.format()