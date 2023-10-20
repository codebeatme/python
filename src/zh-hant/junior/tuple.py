'''
本節文章
https://learnscript.net/zh-hant/python/junior/list-and-tuple/ 什麽是串列，元組？有何不同
'''

###
students = ('小小', '花花', '明明')

###
name = input('請輸入要查詢的學生姓名：')

# 根據學生是否在元組 students 中，顯示不同的資訊
if name in students:
    print('在名單中找到了該學生')
else:
    print('名單中找不到該學生')
