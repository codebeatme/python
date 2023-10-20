'''
JSON是一種結構化資料格式，常見於網路的資訊傳輸
* JSON的書寫格式類似於字典，串列
* JSON可由單個字串，數值，布林值或null組成
* json模組可以編碼或解碼JSON

版本
Python 3.11.2
VSCode 1.76.1

關於本系列教程的使用說明和相關問題解答，請參考文章 https://www.bilibili.com/read/cv23030766
'''

# 匯入模組
import json

# 使用 loads 將 JSON 格式字串轉換為字典
data = json.loads('{"count":2,"news":[{"id":1,"title":"今日天氣"},{"id":2,"title":"明日天氣"}]}')

# 顯示新聞資訊
print(f'共 {data["count"]} 條新聞')

for n in data['news']:
    print(f'id：{n["id"]}，標題：{n["title"]}')

###
id = int(input('請選擇要檢視新聞的 id：'))
# 一個字典，包含了新聞的 id
request_data = {"id": id}

# 將字典轉換為 JSON 格式的字串，然後發送給伺服器
json_string = json.dumps(request_data)
print(f'向伺服器發送 {json_string}')
