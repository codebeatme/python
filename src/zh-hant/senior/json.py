'''
本節文章
https://learnscript.net/zh-hant/python/senior/parse-and-stringify-json/ 如何解析和字串化 JSON
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
