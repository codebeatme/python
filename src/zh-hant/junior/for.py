'''
本節文章
https://learnscript.net/zh-hant/python/junior/for-statement/ 如何使用 for 陳述式
'''

###
students = ['小小', '花花', '明明']

# 教師新增學生，直至輸入了 n
while True:
    print('當前名單：', students)

    name = input('請輸入學生姓名（輸入 n 結束）：')

    if name == 'n':
        break
    else:
        students.append(name)

###
two_count = 0
three_count = 0

# 周遊串列 students 中的所有元素
for name in students:
    # 計算學生姓名的字數，並將對應的變數加 1
    count = len(name)

    if count == 2:
        two_count += 1
    elif count == 3:
        three_count += 1

print(f'兩個字的姓名有 {two_count} 個，三個字的姓名有 {three_count} 個')
