###
import re

while True:
    email = input('请输入邮箱地址：')
    result = re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email)

    if result:
        break

###
text = input('请输入消息：')
result = re.search(r'1[0-9]{10}', text)

if result:
    print(f'是否拨打电话{result.group()}')

###
text = input('请输入消息：')
result = re.sub(r'(哈哈|呵呵)', '**', text)

print(f'过滤后的结果：{result}')