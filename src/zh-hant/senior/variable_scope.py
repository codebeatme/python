'''
本節文章
https://learnscript.net/zh-hant/python/senior/variable-scope/ 變數的範圍
'''

# 在模組中定義表示防禦值的變數 defence
defence = 10

###


def hurt(damage):
    # 函式 hurt，用來造成傷害

    # 這是 hurt 函式定義的 defence
    # defence = 14
    # 根據防禦值來降低傷害值
    damage -= defence

    if damage <= 0:
        return

    def show(text):
        # 巢狀函式 show，用來顯示資訊
        print(text)

    message = f'考慮防禦值後的傷害值為 {damage}'
    show(message)


# 造成 15 點傷害
hurt(15)

# ERROR message 沒有定義
# print(message)
