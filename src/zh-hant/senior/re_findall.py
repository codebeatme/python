'''
規則運算式可用來判斷字串是否匹配某種規則，或尋找取代字串中匹配規則的內容
* match函式可判斷整個字串是否匹配規則
* search函式可尋找字串中匹配規則的部分
* sub函式可取代字串中匹配規則的部分

版本
Python 3.11.2
VSCode 1.76.1

關於本系列教程的使用說明和相關問題解答，請參考文章 https://www.bilibili.com/read/cv23030766
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
