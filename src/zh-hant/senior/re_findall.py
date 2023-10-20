'''
本節文章
https://learnscript.net/zh-hant/python/senior/regular-expressions/ 如何使用規則運算式
'''

# 匯入模組
import re

# 在使用者輸入的訊息中，格式 1xxx 會被識別為電話號碼
text = input('請輸入訊息（1xxx 會被識別為電話號碼）：')
results = re.findall(r'1[0-9]{3}', text)

# 如果存在電話號碼，則提示使用者是否撥打
if results:
    # 顯示所有的電話號碼
    for r in results:
          print(f'找到電話號碼：{r}')
else:
	print('沒有找到電話號碼')
