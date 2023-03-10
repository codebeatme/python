# 视频内容：「Python」高级教程 什么是JSON？JSON的书写格式，JSON与Python对象之间的转换
# 视频地址：https://www.bilibili.com/video/BV1cN411F7Nn/

import json

data = json.loads('{"count":2,"news":[{"id":1,"title":"今日天气"},{"id":2,"title":"明日天气"}]}')

print(f'共{data["count"]}条新闻')

for n in data['news']:
    print(f'id：{n["id"]}，标题：{n["title"]}')

###
id = int(input('请选择要查看新闻的id：'))
request_data = {"id": id}

json_string = json.dumps(request_data)
print(f'向服务器发送{json_string}')
