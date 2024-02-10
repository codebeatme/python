'''
本節文章
https://learnscript.net/zh-hant/python/junior/list-and-tuple/ 什麽是串列，元組？有何不同
'''

###
students = ['小小', '花花', '明明']

###
while True:
    print('當前名單：', students)

    name = input('請輸入學生姓名（輸入 n 結束）：')

    # 輸入 n，執行 break 陳述式跳出迴圈，否則將新增學生到 students 串列
    if name == 'n':
        break
    else:
        students.append(name)
