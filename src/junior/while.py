text = input('请输入多个整数（中间使用空格分割）：')

nums = text.split(' ')
result = 0

while len(nums):
    num = int(nums.pop(0))

    if num < 0:
        continue
    elif num == 0:
        break

    result += num

print(f'这些整数相加的结果为：{result}')