'''
本节文章
https://learnscript.net/zh/python/senior/parse-and-stringify-json/ 如何解析和字符串化 JSON
'''

# 导入模块
import json

# 使用 loads 将 JSON 格式字符串转换为字典
data = json.loads('{"count":2,"news":[{"id":1,"title":"今日天气"},{"id":2,"title":"明日天气"}]}')

# 显示新闻信息
print(f'共 {data["count"]} 条新闻')

for n in data['news']:
    print(f'id：{n["id"]}，标题：{n["title"]}')

###
id = int(input('请选择要查看新闻的 id：'))
# 一个字典，包含了新闻的 id
request_data = {"id": id}

# 将字典转换为 JSON 格式的字符串，然后发送给服务器
json_string = json.dumps(request_data)
print(f'向服务器发送 {json_string}')
