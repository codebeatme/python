'''
本節文章
https://learnscript.net/zh-hant/python/junior/while-statement-and-end-loop/ 如何使用 while 陳述式，結束 while 迴圈
'''

text = input('請輸入多個整數（中間使用空格分割）：')

numbers = text.split(' ')
result = 0

# 如果串列 numbers 包含元素，則重複執行
while len(numbers):
    number = int(numbers.pop(0))

    if number < 0:
        # 不會對負數求和，使用 continue 結束本次迴圈
        continue
    elif number == 0:
        # 遇到 0 則停止求和，使用 break 結束整個迴圈
        break

    # 對所有元素求和，結果儲存在 result 中
    result += number

print(f'這些整數相加的結果為：{result}')
