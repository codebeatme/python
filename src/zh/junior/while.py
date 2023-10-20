'''
本节文章
https://learnscript.net/zh/python/junior/while-statement-and-end-loop/ 如何使用 while 语句，结束 while 循环
'''

text = input('请输入多个整数（中间使用空格分割）：')

numbers = text.split(' ')
result = 0

# 如果列表 numbers 包含元素，则重复执行
while len(numbers):
    number = int(numbers.pop(0))

    if number < 0:
        # 不会对负数求和，使用 continue 结束本次循环
        continue
    elif number == 0:
        # 遇到 0 则停止求和，使用 break 结束整个循环
        break

    # 对所有元素求和，结果保存在 result 中
    result += number

print(f'这些整数相加的结果为：{result}')
