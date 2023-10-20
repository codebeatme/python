'''
本节文章
https://learnscript.net/zh/python/senior/regular-expressions/ 如何使用正则表达式
'''

# 导入模块
import re

# 在用户输入的消息中，格式 1xxx 会被识别为电话号码
text = input('请输入消息（1xxx 会被识别为电话号码）：')
results = re.findall(r'1[0-9]{3}', text)

# 如果存在电话号码，则提示用户是否拨打
if results:
    # 显示所有的电话号码
    for r in results:
          print(f'找到电话号码：{r}')
else:
	print('没有找到电话号码')
